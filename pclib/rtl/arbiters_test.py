#==============================================================================
# arbiters_test.py
#==============================================================================
# This file contains unit tests for the arbiters collection models.

from pymtl      import *
from pclib.test import TestVectorSimulator
from arbiters   import RoundRobinArbiter
from arbiters   import RoundRobinArbiterEn

#------------------------------------------------------------------------------
# run_test
#------------------------------------------------------------------------------
# Test driver for RoundRobinArbiter
def run_test( model, test_vectors ):

  # Instantiate and elaborate the model

  model.elaborate()

  # Define functions mapping the test vector to ports in model

  def tv_in( model, test_vector ):
    model.reqs.value = test_vector[0]

  def tv_out( model, test_vector ):
    assert model.grants == test_vector[1]

  # Run the test

  sim = TestVectorSimulator( model, test_vectors, tv_in, tv_out )
  sim.run_test()

#------------------------------------------------------------------------------
# test_rr_arb_4
#------------------------------------------------------------------------------
# RoundRobinArbiter with four requesters
def test_rr_arb_4( dump_vcd, test_verilog ):
  model = RoundRobinArbiter( 4 )
  model.vcd_file = dump_vcd
  if test_verilog:
    model = TranslationTool( model )

  run_test( model, [

    # reqs     grants
    [ 0b0000,  0b0000 ],

    [ 0b0001,  0b0001 ],
    [ 0b0010,  0b0010 ],
    [ 0b0100,  0b0100 ],
    [ 0b1000,  0b1000 ],

    [ 0b1111,  0b0001 ],
    [ 0b1111,  0b0010 ],
    [ 0b1111,  0b0100 ],
    [ 0b1111,  0b1000 ],
    [ 0b1111,  0b0001 ],

    [ 0b1100,  0b0100 ],
    [ 0b1010,  0b1000 ],
    [ 0b1001,  0b0001 ],
    [ 0b0110,  0b0010 ],
    [ 0b0101,  0b0100 ],
    [ 0b0011,  0b0001 ],

    [ 0b1110,  0b0010 ],
    [ 0b1101,  0b0100 ],
    [ 0b1011,  0b1000 ],
    [ 0b0111,  0b0001 ],

  ])

#------------------------------------------------------------------------------
# run_en_test
#------------------------------------------------------------------------------
# Test driver for RoundRobinArbiterEn
def run_en_test( model, test_vectors ):

  # Instantiate and elaborate the model

  model.elaborate()

  # Define functions mapping the test vector to ports in model

  def tv_in( model, test_vector ):
    model.en.value   = test_vector[0]
    model.reqs.value = test_vector[1]

  def tv_out( model, test_vector ):
    assert model.grants == test_vector[2]

  # Run the test

  sim = TestVectorSimulator( model, test_vectors, tv_in, tv_out )
  sim.run_test()

#------------------------------------------------------------------------------
# test_rr_arb_en_4
#------------------------------------------------------------------------------
# RoundRobinArbiterEn with four requesters
def test_rr_arb_en_4( dump_vcd, test_verilog ):

  model = RoundRobinArbiterEn( 4 )
  model.vcd_file = dump_vcd
  if test_verilog:
    model = TranslationTool( model )

  run_en_test( model, [

    # reqs     grants
    [ 0, 0b0000,  0b0000 ],
    [ 1, 0b0000,  0b0000 ],

    [ 1, 0b0001,  0b0001 ],
    [ 0, 0b0010,  0b0000 ],
    [ 1, 0b0010,  0b0010 ],
    [ 1, 0b0100,  0b0100 ],
    [ 0, 0b1000,  0b0000 ],
    [ 1, 0b1000,  0b1000 ],

    [ 1, 0b1111,  0b0001 ],
    [ 0, 0b1111,  0b0000 ],
    [ 1, 0b1111,  0b0010 ],
    [ 1, 0b1111,  0b0100 ],
    [ 1, 0b1111,  0b1000 ],
    [ 0, 0b1111,  0b0000 ],
    [ 1, 0b1111,  0b0001 ],

    [ 0, 0b1100,  0b0000 ],
    [ 1, 0b1100,  0b0100 ],
    [ 0, 0b1010,  0b0000 ],
    [ 1, 0b1010,  0b1000 ],
    [ 1, 0b1001,  0b0001 ],
    [ 1, 0b0110,  0b0010 ],
    [ 1, 0b0101,  0b0100 ],
    [ 1, 0b0011,  0b0001 ],

    [ 1, 0b1110,  0b0010 ],
    [ 0, 0b1101,  0b0000 ],
    [ 1, 0b1101,  0b0100 ],
    [ 1, 0b1011,  0b1000 ],
    [ 0, 0b0111,  0b0000 ],
    [ 1, 0b0111,  0b0001 ],

  ])
