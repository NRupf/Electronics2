import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge


@cocotb.test()
async def gatetest(dut):
    """Try accessing the design."""

    # set up the clock
    cocotb.start_soon(Clock(dut.clk_i, 20, units='ns').start())
    # Synchronize with the clock
    await FallingEdge(dut.clk_i)

    
    # a and b are inputs to our module
    # c is the output
    
    dut.a_i.value = 1
    dut.b_i.value = 0
    await FallingEdge(dut.clk_i)
    
    dut.a_i.value = 1
    dut.b_i.value = 1
    await FallingEdge(dut.clk_i)
    
    
    dut.a_i.value = 0
    dut.b_i.value = 0
    await FallingEdge(dut.clk_i)
    
    
    dut.a_i.value = 0
    dut.b_i.value = 1
    await FallingEdge(dut.clk_i)
    
    
    
    
    

