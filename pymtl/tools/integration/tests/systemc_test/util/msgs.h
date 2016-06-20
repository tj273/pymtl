#include "defines.h"

#ifndef _MSGS_H_
#define _MSGS_H_


  unsigned const _rd_ = 0;
  unsigned const _wr_ = 1;
  
//#-------------------------------------------------------------------------
//# RoccCoreCmdMsg
//#-------------------------------------------------------------------------
//# Core command messages.
//#
//# Signal names in the list below are used in Rocket chip. They are prefixed
//# with core_cmd_ to indicate signal group and suffixed with _i to indicate
//# their direction is from the core to accelerators.
//#
//# Width   Signal name                 Default value   Description
//#
//#     7   core_cmd_inst_funct_i              funct7   Accelerator instructions
//#     5   core_cmd_inst_rs2_i                   rs2   Source register IDs
//#     5   core_cmd_inst_rs1_i                   rs1   "
//#     1   core_cmd_inst_xd_i                     xd   Set if rd exists
//#     1   core_cmd_inst_xs1_i                   xs1   Set if rs exitsts
//#     1   core_cmd_inst_xs2_i                   xs2   "
//#     5   core_cmd_inst_rd_i                     rd   Destination register ID
//#     7   core_cmd_inst_opcode_i    0x1/0x2/0x3/0x4   Custom instruction opcode
//#    64   core_cmd_rs1_i                   rs1_data   Source register data
//#    64   core_cmd_rs2_i                   rs2_data   Source register data
//#
//# Those signals are arranged in a message format:
//#
//#        7b          5b         5b         1b        1b         1b         5b         7b        64b   64b
//#  +------------+----------+----------+---------+----------+----------+---------+-------------+-----+-----+
//#  | inst_funct | inst_rs2 | inst_rs1 | inst_xd | inst_xs1 | inst_xs2 | inst_rd | inst_opcode | rs1 | rs2 |
//#  +------------+----------+----------+---------+----------+----------+---------+-------------+-----+-----+

  RoccCmdMsg RoccCmd(const sc_biguint<7> &type, const sc_biguint<5> &xr, const sc_biguint<64> &data);
  
  sc_biguint<7>  RoccCmd_type(const RoccCmdMsg &msg);
  
  sc_biguint<5>  RoccCmd_xreg(const RoccCmdMsg &msg);
  
  sc_biguint<64> RoccCmd_data(const RoccCmdMsg &msg);

//#-------------------------------------------------------------------------
//# RoccCoreRespMsg
//#-------------------------------------------------------------------------
//# Core command messages.
//#
//# Signal names in the list below are used in Rocket chip. They are prefixed
//# with core_cmd_ to indicate signal group and suffixed with _i to indicate
//# their direction is from the core to accelerators.
//#
//# Width   Signal name        Default value   Description
//#
//#     7   core_resp_rd_o               rd    Destination register ID in the response
//#    64   core_resp_data_o        rd_data    Destination register data in the response
//#
//# Those signals are arranged in a message format:
//#
//#      5b         64b
//#  +---------+-----------+
//#  | resp_rd | resp_data |
//#  +---------+-----------+
//#

  RoccRespMsg RoccResp(const sc_biguint<64> &data);
  sc_biguint<64> RoccResp_data(const RoccRespMsg &msg);
  
//#-------------------------------------------------------------------------
//# MemReqMsg
//#-------------------------------------------------------------------------
//# Message Format:
//#
//#          opaque  addr               data
//#    3b    nbits   nbits       calc   nbits
//#  +------+------+-----------+------+-----------+
//#  | type |opaque| addr      | len  | data      |
//#  +------+------+-----------+------+-----------+
//#
//# For example, if the opaque field is 8 bits, the address size is 32
//# bits, and the data size is also 32 bits, then the message format is as
//# follows:
//#
//#   76  74 73  66 65       34 33  32 31        0
//#  +------+------+-----------+------+-----------+
//#  | type |opaque| addr      | len  | data      |
//#  +------+------+-----------+------+-----------+

  MemReqMsg MemReq(const sc_uint<3> &type, const sc_uint<32> &addr, const sc_uint<32> &data);
  
  sc_uint<3>  MemReq_type(const MemReqMsg &msg);
  
  sc_uint<32> MemReq_addr(const MemReqMsg &msg);
  
  sc_uint<32> MemReq_data(const MemReqMsg &msg);
  
//#-------------------------------------------------------------------------
//# MemRespMsg
//#-------------------------------------------------------------------------
//# Message Format:
//#
//#          opaque                data
//#    3b    nbits   2b     calc   nbits
//#  +------+------+------+------+-----------+
//#  | type |opaque| test | len  | data      |
//#  +------+------+------+------+-----------+
//#
//# For example, if the opaque field is 8 bits, the address size is 32
//# bits, and the data size is also 32 bits, then the message format is as
//# follows:
//#
//#   46  44 43  36 35  34 33  32 31        0
//#  +------+------+------+------+-----------+
//#  | type |opaque| test | len  | data      |
//#  +------+------+------+------+-----------+

  MemRespMsg MemResp(const sc_uint<3> &type, const sc_uint<32> &data);
  
  sc_uint<3>  MemResp_type(const MemRespMsg &msg);
  
  sc_uint<32> MemResp_data(const MemRespMsg &msg);

#endif

