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

module clock(
	input hlt,
	input clk_in,
	output clk_out);

`ifdef SYNTHESIS
	// Clock gating instance (see in home .ciel/ciel/ihp-sg13g2/versions/.../ihp-sg13g2/libs.ref/sg13g2_stdcell/doc)
	sg13g2_lgcp_1 clock_gate_inst(.GCLK(clk_out), .GATE(~hlt), .CLK(clk_in));
`else
	assign clk_out = (hlt) ? 1'b0 : clk_in;
`endif

endmodule

