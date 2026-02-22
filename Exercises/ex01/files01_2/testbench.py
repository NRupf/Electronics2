import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge

@cocotb.test()
async def test(dut):
    
	# Define inputs and expected responses
	possible_A = [0, 0, 1, 1]
	possible_B = [0, 1, 0, 1]
    
	for i in range(len(possible_A)):
		# Apply stimulus (aka inputs)
		dut.A_i.value = possible_A[i]
		dut.B_i.value = possible_B[i]
		
		# Wait a bit
		await Timer(5, units="ns")
	assert True

