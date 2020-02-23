//////////////////////////////////////////////////////////////////////////////////
// Engineer: VT
// 
// Create Date: 03.02.2019 00:00:39
// Design Name: risc-v 
// Module Name: fetch
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////

module fetch
    #(
        parameter ADDR_WIDTH = 10,
        parameter DATA_WIDTH = 32,
        parameter WORDS = 1024
    )
    (
        input wire clk,
        input wire reset, // not used here
        input wire [ADDR_WIDTH - 1: 0] read_addr,
        input wire [ADDR_WIDTH - 1: 0] write_addr,
        input wire [DATA_WIDTH - 1: 0] write_data,
        input wire write_en,
        output reg [DATA_WIDTH - 1: 0] read_data_reg
    );

    reg [DATA_WIDTH - 1: 0] mem [0: WORDS - 1];

    always @(posedge clk) begin
		read_data_reg <= mem[read_addr];
		if (write_en)
            mem[write_addr] <= write_data;
	end
endmodule
