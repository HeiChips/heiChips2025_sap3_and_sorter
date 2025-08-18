// SPDX-FileCopyrightText: © 2025 Authors
// SPDX-License-Identifier: Apache-2.0

// Based on a module from a previous sorter design from Philippos Papaphilippou, see https://philippos.info/sorter/

// The sorter design needs the following signals:
// 8 bits for the input data (through ui_in)
// 8 bits for the output date (through ui_out)
// 1 bit for valid in and 1 bit for valid out (uio_in[0], uio_out[2])
// 1 bit for flush (to extract the results one by one) (through uio_in[1])

`default_nettype none

`define N 24 // Sorter size, remember to check it in testbench.py in line "N =" as well
`define Width 8

//Modes
`define IDLE 0
`define DESCENDING 1
`define ASCENDING  2
`define FLUSH 3

module Topn_module(clk, nreset, invalidate, mode, data_new, data_new_delayed, shift_in, data_in, valid_in, was_valid_in, shift_out, data_out, valid_out, was_valid_out);

	input clk, nreset, invalidate;
	input [1:0] mode;
	input[`Width-1:0] data_new;
	input[`Width-1:0] data_new_delayed;
	
	input shift_in;	
	input[`Width-1:0] data_in;
	input valid_in;
	input was_valid_in;
	
	output reg shift_out;
	output reg[`Width-1:0] data_out;
	output reg valid_out;
	output reg was_valid_out;

	reg bubble;
	reg pending_flush;
		
	reg [`Width-1:0] current_local;
	reg valid_local;	
	
	always @(posedge clk) begin
	
		if (!nreset) begin
				valid_out<=0;
				was_valid_out<=0;
		
				shift_out<=0;
				valid_local<=0;
				bubble=0;
				pending_flush=0;
				
		end else begin		

			if (invalidate)	begin
				was_valid_out<=valid_out;
			end
			
			current_local=data_out;
			valid_out <= valid_out & !invalidate;		
			
			if ((shift_out==1)) begin 
				
				if ((shift_in==1)) begin
					if ((valid_in==1)) begin	
						current_local = data_in;
						valid_local = valid_in;//1
						//invalidated=0;
						data_out <= data_in;
						was_valid_out <= invalidate;//was_valid_in;//0
						valid_out <= !invalidate;

					end	else begin
						valid_local = 0;						
						data_out <= data_in;
						valid_out <= valid_in;
						was_valid_out <= was_valid_in;						
					end				
				end	else begin			 
					current_local = data_new_delayed;
					valid_local = !invalidate/*d*/;//1
					//invalidated=0;
					was_valid_out <=invalidate;//;0;
					data_out <= data_new_delayed;
					
					valid_out <= !invalidate;
				end										
			end	else begin
				if (pending_flush|(valid_out==0)) begin
					data_out <= data_in;
					
					valid_out <= valid_in;
					was_valid_out <= was_valid_in;
					if ((valid_in==0) && (valid_out==1) && (was_valid_out==0)) begin 
						bubble=1;					
						
					end	
					current_local=data_in;
					valid_local=valid_in;
						
					if ((valid_in==1) && (valid_out==0) /*&& (was_valid_out==1)*/ && (!pending_flush)) begin
						valid_out <=0;
						valid_local=0;
						
					end		
				end else begin 
					valid_local=valid_out;
				end				
			end		
		

			if (((mode==`ASCENDING)|(mode==`DESCENDING)) && (bubble==0) /*&&(was_valid_out==0)&& !invalidate*/) begin				
				if (valid_local && !invalidate ) begin																		
					shift_out <= ((mode==`ASCENDING) & (data_new<=current_local)) | ((mode==`DESCENDING) & (data_new>=current_local));
				end else begin					
					shift_out <=1;
				end					
			end else begin
				shift_out <=0;

			end
			pending_flush<=(mode==`FLUSH);			
		end				
	end
		
endmodule //Topn_module

module sorter(clk, rst, flush, data_i, data_i_v, data_o, data_o_v);
	input clk, rst, flush;
	input [`Width-1:0] data_i;
	input data_i_v;
	output reg [`Width-1:0] data_o;
	output data_o_v;

	wire [`Width-1:0] data_out[`N-1:0];
	wire shift_out[`N-1:0];
	wire valid_out[`N-1:0];
	wire was_valid_out[`N-1:0];
		
	reg[`Width-1:0] data_new_delayed;
	
	assign data_o_v=(was_valid_out[`N-1]);
	
	wire [1:0] mode = data_i_v?`DESCENDING:`IDLE;
		
	always @(mode, valid_out[`N-1],was_valid_out[`N-1], data_out[`N-1], shift_out[`N-1], data_i) begin
		if (was_valid_out[`N-1]|shift_out[`N-1]|(mode==`FLUSH))
			data_o=data_out[`N-1];
		else
			data_o=data_i;				
	end

	genvar i;

	generate
		Topn_module module0(clk, !rst, flush, mode, data_i, data_new_delayed, 1'b0, 0, 1'b0, 1'b0, shift_out[0], data_out[0], valid_out[0], was_valid_out[0]);
    	for (i=1; i<`N; i=i+1) begin
        	Topn_module modules(clk, !rst, flush, mode, data_i, data_new_delayed, shift_out[i-1], data_out[i-1], valid_out[i-1], was_valid_out[i-1], shift_out[i], data_out[i], valid_out[i], was_valid_out[i]);
    	end
	endgenerate
	
	always @(posedge clk) begin
		if (data_i_v)
			data_new_delayed <= data_i;		
	end

endmodule


// Adapted from the Tiny Tapeout template
module heichips25_top_sorter (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

    // List all unused inputs to prevent warnings
    wire _unused = &{ena, uio_in[7:2]};
    assign  uio_out[1:0]=0; assign uio_out[7:3]=0;

    sorter s0(clk, !rst_n, uio_in[0] ,ui_in, uio_in[1],uo_out,uio_out[2] );
    assign uio_oe  = 8'b00100100;

endmodule
