# vcd2csv
Converts selected data from a VCD file into CSV form. 
Each line of the resultant CSV corresponds to a single cycle of execution. 
Cycle times are determined automatically using the CLOCK specifier. 
Uses Verilog\_VCD for VCD parsing, by Gene Sullivan, Sameer Gauria, et. al.: https://pypi.org/project/Verilog\_VCD/ 

## Usage
Running the script requires a VCD file and a list of signals. 
The signal list is provided via a text file, with one signal per line. 
The clock signal (exactly one is allowed) should be followed with "CLOCK" on its line, e.g. "hier.name CLOCK" 
Range specifiers can follow a non-clock line if only one or more subsets should be captured, e.g. "hier.name [15:8] 4 [1:0]" 
Ranges can be in any order, and can overlap 
See example.txt

## Invocation
Requires Python 2.7 
*./vcd2csv.py \<vcd file\> \<txt file with target signal names\> \<output csv name\>*
