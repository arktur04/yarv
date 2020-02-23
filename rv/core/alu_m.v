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
  parameter INSTR_WIDTH = 3,
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
  output reg [DATA_WIDTH - 1: 0] rd1,
  output reg [DATA_WIDTH - 1: 0] rd2,
);

  localparam INSTR_MUL = 0;
  localparam INSTR_MULH = 1;
  localparam INSTR_MULHU = 2;
  localparam INSTR_MULHSU = 3;
  localparam INSTR_DIV = 4;
  localparam INSTR_DIVU = 5;
  localparam INSTR_REM = 6;
  localparam INSTR_REMU = 7;
  
  always@(negedge rst_n, posedge clk)
  if(!rst_n)
    begin
    end
  else
    begin
      case (operation)
        INSTR_MUL: 
        INSTR_MULH: {rd1, rd2} <= rs1 * rs2; 
        INSTR_MULHU:
        INSTR_MULHSU: 
        INSTR_DIV: 
        INSTR_DIVU: 
        INSTR_REM: 
        INSTR_REMU: {rd1, rd2} <= 0; // todo
        default: rd <= 0; // todo: check if we can remove this case for an optimization purpose
      endcase      
    end
endmodule
