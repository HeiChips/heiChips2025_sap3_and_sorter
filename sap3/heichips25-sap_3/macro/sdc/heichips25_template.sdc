###############################################################################
# Created by write_sdc
###############################################################################
current_design heichips25_template
###############################################################################
# Timing Constraints
###############################################################################
create_clock -name clk -period 10.0000 -waveform {0.0000 10.0000} [get_ports {clk}]
set_clock_transition 0.2500 [get_clocks {clk}]
set_clock_uncertainty 0.1500 clk
set_propagated_clock [get_clocks {clk}]
create_generated_clock -name clk_div_two -source [get_ports {clk}] -divide_by 2 [get_pins {_4213_/Q}]
set_propagated_clock [get_clocks {clk_div_two}]
###############################################################################
# Environment
###############################################################################
###############################################################################
# Design Rules
###############################################################################
set_max_transition 3.0000 [current_design]
set_max_capacitance 0.5000 [current_design]
set_max_fanout 8.0000 [current_design]
