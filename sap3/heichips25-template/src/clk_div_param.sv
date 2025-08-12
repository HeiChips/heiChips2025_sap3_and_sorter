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
module clk_div_param #(
    parameter int DIVIDE_BY = 4  // division factor (must be even for 50% duty cycle)
)(
    input  logic clk,
    input  logic rst_n,
    output logic clk_out
);

    // calculate width of counter based on DIVIDE_BY
    localparam int COUNTER_WIDTH = $clog2(DIVIDE_BY);

    logic [COUNTER_WIDTH-1:0] count;

    always_ff @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            count <= '0;
            clk_out <= 1'b0;
        end else begin
            if (count == logic' (DIVIDE_BY/2 - 1)) begin
                clk_out <= ~clk_out;
                count <= 0;
            end else begin
                count <= count + 1;
            end
        end
    end

endmodule
