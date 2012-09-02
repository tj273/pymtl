#=========================================================================
# SorterRTLFlat
#=========================================================================

from pymtl import *

class SorterRTLFlat( Model ):

  def __init__( self ):

    # Input ports

    self.in_0 = InPort(16)
    self.in_1 = InPort(16)
    self.in_2 = InPort(16)
    self.in_3 = InPort(16)

    # Ouput ports

    self.out_0 = OutPort(16)
    self.out_1 = OutPort(16)
    self.out_2 = OutPort(16)
    self.out_3 = OutPort(16)

    # Wires

    self.reg_AB_0 = Wire(16)
    self.reg_AB_1 = Wire(16)
    self.reg_AB_2 = Wire(16)
    self.reg_AB_3 = Wire(16)

    self.B0_max   = Wire(16)
    self.B0_min   = Wire(16)
    self.B1_max   = Wire(16)
    self.B1_min   = Wire(16)

    self.reg_BC_0 = Wire(16)
    self.reg_BC_1 = Wire(16)
    self.reg_BC_2 = Wire(16)
    self.reg_BC_3 = Wire(16)

    self.C0_max   = Wire(16)
    self.C0_min   = Wire(16)
    self.C1_max   = Wire(16)
    self.C1_min   = Wire(16)
    self.C2_max   = Wire(16)
    self.C2_min   = Wire(16)

  #---------------------------------------------------------------------
  # Stage A->B pipeline registers
  #---------------------------------------------------------------------

  @posedge_clk
  def reg_ab( self ):
    self.reg_AB_0.next = self.in_0.value
    self.reg_AB_1.next = self.in_1.value
    self.reg_AB_2.next = self.in_2.value
    self.reg_AB_3.next = self.in_3.value

  #---------------------------------------------------------------------
  # Stage B combinational logic
  #---------------------------------------------------------------------

  @combinational
  def stage_b( self ):
    if self.reg_AB_0.value >= self.reg_AB_1.value:
      self.B0_max.value = self.reg_AB_0.value
      self.B0_min.value = self.reg_AB_1.value
    else:
      self.B0_max.value = self.reg_AB_1.value
      self.B0_min.value = self.reg_AB_0.value

    if self.reg_AB_2.value >= self.reg_AB_3.value:
      self.B1_max.value = self.reg_AB_2.value
      self.B1_min.value = self.reg_AB_3.value
    else:
      self.B1_max.value = self.reg_AB_3.value
      self.B1_min.value = self.reg_AB_2.value

  #---------------------------------------------------------------------
  # Stage B->C pipeline registers
  #---------------------------------------------------------------------

  @posedge_clk
  def reg_bc( self ):
    self.reg_BC_0.next = self.B0_min.value
    self.reg_BC_1.next = self.B0_max.value

    self.reg_BC_2.next = self.B1_min.value
    self.reg_BC_3.next = self.B1_max.value

  #---------------------------------------------------------------------
  # Stage C combinational logic
  #---------------------------------------------------------------------

  @combinational
  def stage_c( self ):
    if self.reg_BC_0.value >= self.reg_BC_2.value:
      self.C0_max.value = self.reg_BC_0.value
      self.C0_min.value = self.reg_BC_2.value
    else:
      self.C0_max.value = self.reg_BC_2.value
      self.C0_min.value = self.reg_BC_0.value

    if self.reg_BC_1.value >= self.reg_BC_3.value:
      self.C1_max.value = self.reg_BC_1.value
      self.C1_min.value = self.reg_BC_3.value
    else:
      self.C1_max.value = self.reg_BC_3.value
      self.C1_min.value = self.reg_BC_1.value

    if self.C0_max.value >= self.C1_min.value:
      self.C2_max.value = self.C0_max.value
      self.C2_min.value = self.C1_min.value
    else:
      self.C2_max.value = self.C1_min.value
      self.C2_min.value = self.C0_max.value

    # Connect to output ports

    self.out_0.value = self.C0_min.value
    self.out_1.value = self.C2_min.value
    self.out_2.value = self.C2_max.value
    self.out_3.value = self.C1_max.value
