module gate(
	input a_i,
	input b_i,
	output c_o,
	input clk_i
	);
	
	assign c_o = a_i && b_i;
	
endmodule
