//////////////////////////////////////////////////////////////////////////////////
// Engineer: VT
// 
// Create Date: 22.02.2020 
// Design Name: risc-v 
// Module Name: alu_i
// Project Name: yarv
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments: this file is for synthesys alu_i in vivado, for time analysis
// 
//////////////////////////////////////////////////////////////////////////////////


module alu_i_synth
#(
  parameter INSTR_WIDTH = 4,
  parameter DATA_WIDTH = 32
)
(
  input wire rst_n,
  input wire clk,
  // operands and opcode
  input wire [DATA_WIDTH - 1: 0] rs1,
  input wire [DATA_WIDTH - 1: 0] rs2,
  input wire [INSTR_WIDTH - 1: 0] operation,
  // result
  output wire [DATA_WIDTH - 1: 0] rd
);
  reg [DATA_WIDTH - 1: 0] rs1_reg;
  reg [DATA_WIDTH - 1: 0] rs2_reg;
  reg [INSTR_WIDTH - 1: 0] operation_reg;

  always@(posedge clk)
  begin
    rs1_reg <= rs1;
    rs2_reg <= rs2;
    operation_reg <= operation;
  end

  alu_i i_alu_i
  (
    .rst_n(rst_n),
    .clk(clk),
    // operands and opcode
    .rs1(rs1_reg),
    .rs2(rs2_reg),
    .operation(operation_reg),
    // result
    .rd_reg(rd)
  );
endmodule
