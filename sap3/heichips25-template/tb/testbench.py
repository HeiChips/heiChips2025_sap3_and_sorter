# SPDX-FileCopyrightText: © 2025 XXX Authors
# SPDX-License-Identifier: Apache-2.0

import os
import sys
from pathlib import Path
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, Edge
from cocotb.runner import get_runner
from cocotb.triggers import Timer, ClockCycles


@cocotb.test()
async def sap_three_test_output(dut):
    """Testing the counter of the design."""
    
    # Create a clock with a period of 10ns = 100MHz
    clock = Clock(dut.clk, 10, 'ns')
    await cocotb.start(clock.start())

    dut.io_in.value  = 0

    # Reset the design for 100ns
    dut.io_in.value = 0
    await Timer(100, 'ns')
    dut.io_in.value = 1
    await Timer(100, 'ns')

    # Wait for 100 clock cycles
    await ClockCycles(dut.clk, 100)

    # Ensure the output is 0x01
    print(f"The current output is: {dut.heichips25_template_inst.sap_3_outputReg.value}, and should be: 0x01")
    assert dut.heichips25_template_inst.sap_3_outputReg == 1, "Output is not 1!"

    # Wait for 100 clock cycles
    await ClockCycles(dut.clk, (100))

    # Ensure the output is 0x02
    print(f"The current output is: {dut.heichips25_template_inst.sap_3_outputReg.value}, and should be: 0x02")
    assert dut.heichips25_template_inst.sap_3_outputReg == 2, "Output is not 2!"

    # Wait for 100 clock cycles
    await ClockCycles(dut.clk, (100))

    # Ensure the output is 0x04
    print(f"The current output is: {dut.heichips25_template_inst.sap_3_outputReg.value}, and should be: 0x04")
    assert dut.heichips25_template_inst.sap_3_outputReg == 4, "Output is not 4!"

    # Wait for 100 clock cycles
    await ClockCycles(dut.clk, (100))

    # Ensure the output is 0x08
    print(f"The current output is: {dut.heichips25_template_inst.sap_3_outputReg.value}, and should be: 0x08")
    assert dut.heichips25_template_inst.sap_3_outputReg == 8, "Output is not 8!"

    # Wait for 100 clock cycles
    await ClockCycles(dut.clk, (120))

    # Ensure the output is 0x10
    print(f"The current output is: {dut.heichips25_template_inst.sap_3_outputReg.value}, and should be: 0x10")
    assert dut.heichips25_template_inst.sap_3_outputReg == 16, "Output is not 16!"

    # Wait for 100 clock cycles
    await ClockCycles(dut.clk, (120))

    # Ensure the output is 0x20
    print(f"The current output is: {dut.heichips25_template_inst.sap_3_outputReg.value}, and should be: 0x20")
    assert dut.heichips25_template_inst.sap_3_outputReg == 32, "Output is not 32!"

    # Wait for 50 clock cycles
    await ClockCycles(dut.clk, (140))

    # Ensure the output is 0x40
    print(f"The current output is: {dut.heichips25_template_inst.sap_3_outputReg.value}, and should be: 0x40")
    assert dut.heichips25_template_inst.sap_3_outputReg == 64, "Output is not 64!"

    # Wait for 50 clock cycles
    await ClockCycles(dut.clk, (180))

    # Ensure the output is 0x80
    print(f"The current output is: {dut.heichips25_template_inst.sap_3_outputReg.value}, and should be: 0x80")
    assert dut.heichips25_template_inst.sap_3_outputReg == 128, "Output is not 128!"

    # Wait for 50 clock cycles
    await ClockCycles(dut.clk, (140))

    # Ensure the output is 0x40
    print(f"The current output is: {dut.heichips25_template_inst.sap_3_outputReg.value}, and should be: 0x40")
    assert dut.heichips25_template_inst.sap_3_outputReg == 64, "Output is not 64!"

    # Wait for 100 clock cycles
    await ClockCycles(dut.clk, (100))

    # Ensure the output is 0x20
    print(f"The current output is: {dut.heichips25_template_inst.sap_3_outputReg.value}, and should be: 0x20")
    assert dut.heichips25_template_inst.sap_3_outputReg == 32, "Output is not 32!"

    # Wait for 100 clock cycles
    await ClockCycles(dut.clk, (100))

    # Ensure the output is 0x10
    print(f"The current output is: {dut.heichips25_template_inst.sap_3_outputReg.value}, and should be: 0x10")
    assert dut.heichips25_template_inst.sap_3_outputReg == 16, "Output is not 16!"

    # Wait for 100 clock cycles
    await ClockCycles(dut.clk, (100))

    # Ensure the output is 0x08
    print(f"The current output is: {dut.heichips25_template_inst.sap_3_outputReg.value}, and should be: 0x08")
    assert dut.heichips25_template_inst.sap_3_outputReg == 8, "Output is not 8!"

    # Wait for 100 clock cycles
    await ClockCycles(dut.clk, (140))

    # Ensure the output is 0x04
    print(f"The current output is: {dut.heichips25_template_inst.sap_3_outputReg.value}, and should be: 0x04")
    assert dut.heichips25_template_inst.sap_3_outputReg == 4, "Output is not 4!"

    # Wait for 100 clock cycles
    await ClockCycles(dut.clk, (100))

    # Ensure the output is 0x02
    print(f"The current output is: {dut.heichips25_template_inst.sap_3_outputReg.value}, and should be: 0x02")
    assert dut.heichips25_template_inst.sap_3_outputReg == 2, "Output is not 2!"

    # Wait for 100 clock cycles
    await ClockCycles(dut.clk, (100))

    # Ensure the output is 0x01
    print(f"The current output is: {dut.heichips25_template_inst.sap_3_outputReg.value}, and should be: 0x01")
    assert dut.heichips25_template_inst.sap_3_outputReg == 1, "Output is not 1!"


    # Wait for 200 clock cycles
    await ClockCycles(dut.clk, (400))

    # cocotb documentation: https://docs.cocotb.org/en/stable/refcard.html
    # cocotb reference card: https://docs.cocotb.org/en/stable/refcard.html

@cocotb.test()
async def sap_three_test_serializer(dut):
    
    # Clock starten
    clock = Clock(dut.clk, 10, 'ns')
    await cocotb.start(clock.start())

    # Reset
    dut.io_in.value = 0
    await Timer(50, 'ns')
    dut.io_in.value = 1
    await Timer(50, 'ns')

    
    await Timer(1, 'us')
    print(f"rx.data_out with: {dut.rx.data_out.value} should match the shadow register value the shadow register value {dut.heichips25_template_inst.u_ser.shadow_reg.value}")
    assert dut.heichips25_template_inst.u_ser.shadow_reg.value == dut.rx.data_out.value, "Should be equal!"
    await Timer(1, 'us')
    print(f"rx.data_out with: {dut.rx.data_out.value} should match the shadow register value {dut.heichips25_template_inst.u_ser.shadow_reg.value}")
    assert dut.heichips25_template_inst.u_ser.shadow_reg.value == dut.rx.data_out.value, "Should be equal!"
    await Timer(1.5, 'us')
    print(f"rx.data_out with: {dut.rx.data_out.value} should match the shadow register value {dut.heichips25_template_inst.u_ser.shadow_reg.value}")
    assert dut.heichips25_template_inst.u_ser.shadow_reg.value == dut.rx.data_out.value, "Should be equal!"
    await Timer(1, 'us')
    print(f"rx.data_out with: {dut.rx.data_out.value} should match the shadow register value {dut.heichips25_template_inst.u_ser.shadow_reg.value}")
    assert dut.heichips25_template_inst.u_ser.shadow_reg.value == dut.rx.data_out.value, "Should be equal!"
    await Timer(1, 'us')
    print(f"rx.data_out with: {dut.rx.data_out.value} should match the shadow register value {dut.heichips25_template_inst.u_ser.shadow_reg.value}")
    assert dut.heichips25_template_inst.u_ser.shadow_reg.value == dut.rx.data_out.value, "Should be equal!"
    await Timer(1.5, 'us')
    print(f"rx.data_out with: {dut.rx.data_out.value} should match the shadow register value {dut.heichips25_template_inst.u_ser.shadow_reg.value}")
    assert dut.heichips25_template_inst.u_ser.shadow_reg.value == dut.rx.data_out.value, "Should be equal!"
    await Timer(1, 'us')
    print(f"rx.data_out with: {dut.rx.data_out.value} should match the shadow register value {dut.heichips25_template_inst.u_ser.shadow_reg.value}")
    assert dut.heichips25_template_inst.u_ser.shadow_reg.value == dut.rx.data_out.value, "Should be equal!"
    await Timer(2, 'us')
    print(f"rx.data_out with: {dut.rx.data_out.value} should match the shadow register value {dut.heichips25_template_inst.u_ser.shadow_reg.value}")
    assert dut.heichips25_template_inst.u_ser.shadow_reg.value == dut.rx.data_out.value, "Should be equal!"
    await Timer(1, 'us')
    print(f"rx.data_out with: {dut.rx.data_out.value} should match the shadow register value {dut.heichips25_template_inst.u_ser.shadow_reg.value}")
    assert dut.heichips25_template_inst.u_ser.shadow_reg.value == dut.rx.data_out.value, "Should be equal!"
    await Timer(1, 'us')
    print(f"rx.data_out with: {dut.rx.data_out.value} should match the shadow register value {dut.heichips25_template_inst.u_ser.shadow_reg.value}")
    assert dut.heichips25_template_inst.u_ser.shadow_reg.value == dut.rx.data_out.value, "Should be equal!"
    await Timer(1, 'us')
    print(f"rx.data_out with: {dut.rx.data_out.value} should match the shadow register value {dut.heichips25_template_inst.u_ser.shadow_reg.value}")
    assert dut.heichips25_template_inst.u_ser.shadow_reg.value == dut.rx.data_out.value, "Should be equal!"
    await Timer(1, 'us')
    print(f"rx.data_out with: {dut.rx.data_out.value} should match the shadow register value {dut.heichips25_template_inst.u_ser.shadow_reg.value}")
    assert dut.heichips25_template_inst.u_ser.shadow_reg.value == dut.rx.data_out.value, "Should be equal!"
    await Timer(1, 'us')
    print(f"rx.data_out with: {dut.rx.data_out.value} should match the shadow register value {dut.heichips25_template_inst.u_ser.shadow_reg.value}")
    assert dut.heichips25_template_inst.u_ser.shadow_reg.value == dut.rx.data_out.value, "Should be equal!"
    await Timer(1, 'us')
    print(f"rx.data_out with: {dut.rx.data_out.value} should match the shadow register value {dut.heichips25_template_inst.u_ser.shadow_reg.value}")
    assert dut.heichips25_template_inst.u_ser.shadow_reg.value == dut.rx.data_out.value, "Should be equal!"
    await Timer(2, 'us')
    print(f"rx.data_out with: {dut.rx.data_out.value} should match the shadow register value {dut.heichips25_template_inst.u_ser.shadow_reg.value}")
    assert dut.heichips25_template_inst.u_ser.shadow_reg.value == dut.rx.data_out.value, "Should be equal!"
    await Timer(1, 'us')
    print(f"rx.data_out with: {dut.rx.data_out.value} should match the shadow register value {dut.heichips25_template_inst.u_ser.shadow_reg.value}")
    assert dut.heichips25_template_inst.u_ser.shadow_reg.value == dut.rx.data_out.value, "Should be equal!"
    await Timer(1, 'us')
    print(f"rx.data_out with: {dut.rx.data_out.value} should match the shadow register value {dut.heichips25_template_inst.u_ser.shadow_reg.value}")
    assert dut.heichips25_template_inst.u_ser.shadow_reg.value == dut.rx.data_out.value, "Should be equal!"

@cocotb.test()
async def sap_three_test_array_serializer(dut):

    print("****************************************************************************************************** \n" \
          "* This test tests the serialization of the register file which is implemented to debug the processor * \n" \
          "****************************************************************************************************** \n")

    # Clock starten
    clock = Clock(dut.clk, 10, 'ns')
    await cocotb.start(clock.start())

    # Reset
    dut.io_in.value = 0
    await Timer(50, 'ns')
    dut.io_in.value = 1
    await Timer(50, 'ns')

    # check reg 7 for given program code
    await Timer(848, 'ns')
    reg7 = dut.heichips25_template_inst.sap_3_inst.reg_file.array_serializer_inst.shadow_reg.value
    await Timer(953-848, 'ns')
    assert dut.array_deserializer_inst.data_out.value == reg7, "Should be equal!"

    # check reg 11 for given program code
    await Timer(2457-953, 'ns')
    reg11 = dut.heichips25_template_inst.sap_3_inst.reg_file.array_serializer_inst.shadow_reg.value
    await Timer(2554-2457, 'ns')
    assert dut.array_deserializer_inst.data_out.value == reg11, "Should be equal!"

    # check reg 9 for given program code
    await Timer(19049, 'ns')
    reg9 = dut.heichips25_template_inst.sap_3_inst.reg_file.array_serializer_inst.shadow_reg.value
    await Timer(19152-19049, 'ns')
    assert dut.array_deserializer_inst.data_out.value == reg9, "Should be equal!"

@cocotb.test()
async def sap_three_test_memory(dut):

    print("****************************************************************************************************** \n" \
          "* Simple Memory / Processor test                                                                     * \n" \
          "****************************************************************************************************** \n")

    # Clock starten
    clock = Clock(dut.clk, 10, 'ns')
    await cocotb.start(clock.start())

    # Reset
    dut.io_in.value = 0
    await Timer(50, 'ns')
    dut.io_in.value = 1
    await Timer(50, 'ns')

    # Expected instructions
    expected_bytes = [
        0xf0, 0x00, 0x3e, 0x01, 0x06, 0x00, 0xd3, 0x4f, 0x78, 0xfe, 0x01, 0x79, 0xca, 0xc2, 0x20    ]

    index = 0
    last_value = None

    while index < len(expected_bytes):
        # Wait for signal to change
        await Edge(dut.IHP_SRAM_1024x32_wrapper.DOUT)

        current_value = int(dut.IHP_SRAM_1024x32_wrapper.DOUT.value)

        # If the signal remains the same, skip
        if current_value == last_value:
            continue
        last_value = current_value

        expected_value = expected_bytes[index]
        assert current_value == expected_value, \
            f"Instruction byte {index} does not match: expected {expected_value:#04x}, got {current_value:#04x}"

        print(f"[OK] Byte {index}: {current_value:#04x}")
        index += 1

    print("All instruction bytes were correctly output!")


if __name__ == "__main__":

    sim         = os.getenv("SIM", "icarus")
    pdk_root    = os.getenv("PDK_ROOT", "~/.ciel")
    pdk         = os.getenv("PDK", "ihp-sg13g2")
    scl         = os.getenv("SCL", "sg13g2_stdcell")
    gl          = os.getenv("GL", False)

    testbench_path = Path(__file__).resolve().parent
    sources = []#[testbench_path / 'testbench.sv']
    defines = {}

    MACRO_NL = testbench_path / '../macro/nl/heichips25_template.nl.v'

    if gl:
        if not MACRO_NL.exists():
            print(f"The macro netlist {MACRO_NL} does not exist. Did you implement the macro?")
            sys.exit(0)
    
        sources.append(Path(pdk_root).expanduser() / pdk / "libs.ref" / scl / "verilog" / f"{scl}.v" )
        sources.append(MACRO_NL)
        defines = {'FUNCTIONAL': True, 'UNIT_DELAY': '#0'}
    else:
        sources.extend(list(testbench_path.glob('../src/*')))
        #print(f"Using sources: {sources}") # debug
        defines = {'RTL': True}

    hdl_toplevel = "top_tb"

    runner = get_runner(sim)
    runner.build(
        sources=sources,
        hdl_toplevel=hdl_toplevel,
        defines=defines,
        timescale=['1ns', '1ps'],
        waves=True,
        build_args=['--trace', '--trace-fst', '--trace-structs'] if sim == 'verilator' else ['-gno-specify'],
    )

    runner.test(
        hdl_toplevel=hdl_toplevel,
        test_module='testbench,',
        timescale=['1ns', '1ps'],
        waves=True,
        plusargs=['--trace-file', f'{hdl_toplevel}.fst']  if sim == 'verilator' else [],
    )
