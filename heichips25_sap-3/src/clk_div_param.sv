/*
 * This file is part of heichips25_sap3, licensed under the Apache License, Version 2.0.
 * See the LICENSE file in the project root for full license text.
 *
 * Portions of this file are derived from the SAP processor implementation
 * by Austin Morlan, licensed under the MIT License (MIT).
 * See the LICENSE file in the project root for the full MIT License text.
 *
 * Modifications © [2025] [Moritz Schridde, Enrica Schmidt, Philippos Papaphilippou, Deepak Bathija, Malte Bauer]
 */
//------------------------------------------------------------------------------
//  Module: clk_div_param
//  Description:
//      Parameterized clock divider with synchronous active-low reset.
//      Generates a divided clock output (clk_out) from the input clock (clk).
//      The division factor is set by the DIVIDE_BY parameter (must be even for
//      a 50% duty cycle). The output clock toggles every DIVIDE_BY/2 cycles.
//
//  Parameters:
//      DIVIDE_BY (int) - Division factor for the clock (default: 4).
//
//  Ports:
//      input  logic clk     - Input clock signal.
//      input  logic rst_n   - Asynchronous active-low reset.
//      output logic clk_out - Divided clock output.
//
//------------------------------------------------------------------------------
module clk_div_param (
    input  logic clk,
    input  logic rst_n,
    output logic clk_out
);
    logic clk_out_reg;

    localparam DIVIDE_BY = 2;

    // calculate width of counter based on DIVIDE_BY
    localparam int COUNTER_WIDTH = $clog2(DIVIDE_BY);

    logic [COUNTER_WIDTH-1:0] count;

    always_ff @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            count <= '0;
            clk_out_reg <= 1'b0;
        end else begin
            if (count == DIVIDE_BY/2 - 1) begin
                clk_out_reg <= ~clk_out_reg;
                count <= 0;
            end else begin
                count <= count + 1;
            end
        end
    end
    
   sg13g2_buf_16 clock_root (
    .A(clk_out_reg),
    .X(clk_out)
   );

endmodule
