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
// Additional Comments: tis file implements the "I" part of the RISC V ISA
// 
//////////////////////////////////////////////////////////////////////////////////
module alu_i 
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
  output reg [DATA_WIDTH - 1: 0] rd_reg
);

  localparam INSTR_ADD = 0;
  localparam INSTR_SLT = 1;
  localparam INSTR_SLTU = 2;
  localparam INSTR_AND = 3;
  localparam INSTR_OR = 4;
  localparam INSTR_XOR = 5;
  localparam INSTR_SLL = 6;
  localparam INSTR_SRL = 7;
  localparam INSTR_SUB = 8;
  localparam INSTR_SRA = 9;
  
  always@(negedge rst_n, posedge clk)
  if(!rst_n)
    begin
    end
  else
    begin
      //todo   
    end
endmodule
