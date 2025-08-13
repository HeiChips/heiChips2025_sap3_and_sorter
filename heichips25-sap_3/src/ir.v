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

module ir(
	input clk,
	input rst,
	input we,
	input[7:0] bus,
	output[7:0] out
);

reg[7:0] ir;

always @(posedge clk, posedge rst) begin
	if (rst) begin
		ir <= 8'b0;
	end else if (we) begin
		ir <= bus;
	end
end

assign out = ir;

endmodule

