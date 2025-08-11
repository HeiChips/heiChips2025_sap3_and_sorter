module clock(
	input hlt,
	input clk_in,
	output clk_out);

// Clock gating instance (see in home .ciel/ciel/ihp-sg13g2/versions/.../ihp-sg13g2/libs.ref/sg13g2_stdcell/doc)
sg13g2_lgcp_1 clock_gate_inst(.GCLK(clk_out), .GATE(hlt), .CLK(clk_in));


endmodule

