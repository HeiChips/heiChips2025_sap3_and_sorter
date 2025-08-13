module deserializer #(
    parameter WIDTH = 8
) (
    input  logic             clk,
    input  logic             rst,
    input  logic             serial_in,  // serial data stream from serializer
    input  logic             start,      // Start signal from serializer (1 clock before bit 0)
    output logic [WIDTH-1:0] data_out,    // parallel output
    output logic             synced      // High during reception
);

    logic [$clog2(WIDTH)-1:0] bit_cnt;
    logic [WIDTH-1:0]         shift_reg;
    logic                     start_d; // delayed start signal

    always_ff @(posedge clk or posedge rst) begin
        if (rst) begin
            bit_cnt    <= '0;
            shift_reg  <= '0;
            data_out   <= '0;
            synced     <= 1'b0;
            start_d    <= 1'b0;
        end else begin
            start_d <= start; // delayed start signal

            if (start) begin
                // Preparation: Reset counter, but don't take in any bits yet
                bit_cnt <= 0;
                synced  <= 1'b1;
            end else if (synced) begin
                // First bit comes directly after start pulse
                shift_reg[bit_cnt] <= serial_in;

                if (bit_cnt == WIDTH-1) begin
                    data_out <= shift_reg;
                    synced   <= 1'b0; // Reception complete
                end else begin
                    bit_cnt <= bit_cnt + 1;
                end
            end
        end
    end

endmodule

