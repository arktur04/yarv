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
  output reg [DATA_WIDTH - 1: 0] rd
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
      case (operation)
        INSTR_ADD: rd <= rs1 + rs2;
        INSTR_SLT: if($signed(rs1) < $signed(rs2))
            rd <= 1'b1;
          else
            rd <= 1'b0;
        INSTR_SLTU: if(rs1 < rs2)
            rd <= 1'b1;
          else
            rd <= 1'b0;
        INSTR_AND: rd <= rs1 & rs2;
        INSTR_OR: rd <= rs1 | rs2;
        INSTR_XOR: rd <= rs1 ^ rs2;
        INSTR_SLL: rd <= rs1 << rs2;
        INSTR_SRL: rd <= rs1 >> rs2;
        INSTR_SUB: rd <= rs1 - rs2;
        INSTR_SRA: rd <= rs1 >>> rs2;
        default: rd <= 0; // todo: check if we can remove this case for an optimization purpose
      endcase      
    end
endmodule
