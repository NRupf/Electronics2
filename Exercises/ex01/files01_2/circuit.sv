module circuit(
	input logic A_i,
	input logic B_i,
	output logic C_o,
	output logic D_o
	);
      
   // Write your logic here
   assign C_o = A_i && B_i;

   assign D_o = C_o || B_i;
   
endmodule
