module instr_fetch_top
#(
  parameter INSTR_FETCH_ADDR_WIDTH = 32,
  parameter INSTR_FETCH_DATA_WIDTH = 32
)
(
  input wire rst_n,
  input wire clk,
  input wire [INSTR_FETCH_ADDR_WIDTH - 1: 0] instr_fetch_addr_wr,
  input wire [INSTR_FETCH_DATA_WIDTH - 1: 0] instr_fetch_data_wr,
  input wire instr_fetch_wr,
  input wire [INSTR_FETCH_ADDR_WIDTH - 1: 0] instr_fetch_addr0_rd,
  input wire instr_fetch0_rd,
  input wire [INSTR_FETCH_ADDR_WIDTH - 1: 0] instr_fetch_addr1_rd,
  input wire instr_fetch1_rd,
  output wire [INSTR_FETCH_DATA_WIDTH - 1: 0] instr_fetch_data0_rd,
  output wire [INSTR_FETCH_DATA_WIDTH - 1: 0] instr_fetch_data1_rd
);

reg [INSTR_FETCH_ADDR_WIDTH - 1: 0] instr_fetch_addr_wr_reg;
reg [INSTR_FETCH_DATA_WIDTH - 1: 0] instr_fetch_data_wr_reg;
reg instr_fetch_wr_reg;
reg [INSTR_FETCH_ADDR_WIDTH - 1: 0] instr_fetch_addr0_rd_reg;
reg [INSTR_FETCH_DATA_WIDTH - 1: 0] instr_fetch0_rd_reg;
reg [INSTR_FETCH_ADDR_WIDTH - 1: 0] instr_fetch_addr1_rd_reg;
reg [INSTR_FETCH_DATA_WIDTH - 1: 0] instr_fetch1_rd_reg;

  always@(negedge rst_n, posedge clk)
  begin
    if(!rst_n)
    begin
      instr_fetch_addr_wr_reg <= 0;
      instr_fetch_data_wr_reg <= 0;
      instr_fetch_wr_reg <= 0;
      instr_fetch_addr0_rd_reg <= 0;
      instr_fetch0_rd_reg <= 0;
      instr_fetch_addr1_rd_reg <= 0;
      instr_fetch1_rd_reg <= 0;
    end
    else
    begin
      instr_fetch_addr_wr_reg <= instr_fetch_addr_wr;
      instr_fetch_data_wr_reg <= instr_fetch_data_wr;
      instr_fetch_wr_reg <= instr_fetch_wr;
      instr_fetch_addr0_rd_reg <= instr_fetch_addr0_rd;
      instr_fetch0_rd_reg <= instr_fetch0_rd;
      instr_fetch_addr1_rd_reg <= instr_fetch_addr1_rd;
      instr_fetch1_rd_reg <= instr_fetch1_rd;
    end
  end

instr_fetch instr_fetch_i(
  //input wire rst_n, // rst_n is not used yet
  .clk(clk),
  // write interface
  .instr_fetch_addr_wr(instr_fetch_addr_wr_reg),
  .instr_fetch_data_wr(instr_fetch_data_wr_reg),
  .instr_fetch_wr(instr_fetch_wr_reg),
  // primary read interface
  .instr_fetch_addr0_rd(instr_fetch_addr0_rd_reg),
  .instr_fetch0_rd(instr_fetch0_rd_reg),
  .instr_fetch_data0_rd_reg(instr_fetch_data0_rd),
  // secondary read interface
  .instr_fetch_addr1_rd(instr_fetch_addr1_rd_reg),
  .instr_fetch1_rd(instr_fetch1_rd_reg),
  .instr_fetch_data1_rd_reg(instr_fetch_data1_rd)
);

endmodule
