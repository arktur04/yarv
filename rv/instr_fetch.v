module instr_fetch 
#(
  parameter INSTR_FETCH_ADDR_WIDTH = 32,
  parameter INSTR_FETCH_DATA_WIDTH = 32
)
(
  //input wire rst_n, // rst_n is not used yet
  input wire clk,
  // write interface
  input wire [INSTR_FETCH_ADDR_WIDTH - 1: 0] instr_fetch_addr_wr,
  input wire [INSTR_FETCH_DATA_WIDTH - 1: 0] instr_fetch_data_wr,
  input wire instr_fetch_wr,
  // primary read interface
  input wire [INSTR_FETCH_ADDR_WIDTH - 1: 0] instr_fetch_addr0_rd,
  input wire instr_fetch0_rd,
  output reg [INSTR_FETCH_DATA_WIDTH - 1: 0] instr_fetch_data0_rd_reg,
  // secondary read interface
  input wire [INSTR_FETCH_ADDR_WIDTH - 1: 0] instr_fetch_addr1_rd,
  input wire instr_fetch1_rd,
  output reg [INSTR_FETCH_DATA_WIDTH - 1: 0] instr_fetch_data1_rd_reg
);

  localparam INSTR_CACHE_SIZE = 1024;
  // the instruction cache
  reg [INSTR_FETCH_DATA_WIDTH - 1: 0] ram[0: INSTR_CACHE_SIZE - 1];

  // port A
  always@(posedge clk)
  begin
    if(instr_fetch_wr)
    begin
      ram[instr_fetch_addr_wr] <= instr_fetch_data_wr;
    end
    else
    begin
      if(instr_fetch0_rd)
      begin
        instr_fetch_data0_rd_reg <= ram[instr_fetch_addr0_rd];
      end
    end
  end

  // port B
  always@(posedge clk)
  begin
    if(instr_fetch1_rd)
    begin
      instr_fetch_data1_rd_reg <= ram[instr_fetch_addr1_rd];
    end
  end

endmodule
