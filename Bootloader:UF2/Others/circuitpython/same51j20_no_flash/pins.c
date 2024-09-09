#include "shared-bindings/board/__init__.h"

STATIC const mp_rom_map_elem_t board_module_globals_table[] = {
    CIRCUITPYTHON_BOARD_DICT_STANDARD_ITEMS

    { MP_ROM_QSTR(MP_QSTR_IsoNegAnalogIn), MP_ROM_PTR(&pin_PA02) },
    
    { MP_ROM_QSTR(MP_QSTR_VREF), MP_ROM_PTR(&pin_PA03) },

    { MP_ROM_QSTR(MP_QSTR_A0), MP_ROM_PTR(&pin_PA04) },

    { MP_ROM_QSTR(MP_QSTR_IsoPosAnalogIn), MP_ROM_PTR(&pin_PA05) },
    
    { MP_ROM_QSTR(MP_QSTR_A1), MP_ROM_PTR(&pin_PA06) },
  
    { MP_ROM_QSTR(MP_QSTR_SDA), MP_ROM_PTR(&pin_PA12) },
   
    { MP_ROM_QSTR(MP_QSTR_SCL), MP_ROM_PTR(&pin_PA13) },

    { MP_ROM_QSTR(MP_QSTR_DO1), MP_ROM_PTR(&pin_PA14) },
 
    { MP_ROM_QSTR(MP_QSTR_DO2), MP_ROM_PTR(&pin_PA16) },
  
    { MP_ROM_QSTR(MP_QSTR_SCK), MP_ROM_PTR(&pin_PA17) },

    { MP_ROM_QSTR(MP_QSTR_RelayNeg), MP_ROM_PTR(&pin_PA18) },

    { MP_ROM_QSTR(MP_QSTR_RelayPos), MP_ROM_PTR(&pin_PA19) },

    { MP_ROM_QSTR(MP_QSTR_D0), MP_ROM_PTR(&pin_PA20) },

    { MP_ROM_QSTR(MP_QSTR_D1), MP_ROM_PTR(&pin_PA21) },

    { MP_ROM_QSTR(MP_QSTR_D2), MP_ROM_PTR(&pin_PA22) },

    { MP_ROM_QSTR(MP_QSTR_D3), MP_ROM_PTR(&pin_PA23) },

    { MP_ROM_QSTR(MP_QSTR_BatteryMonitor), MP_ROM_PTR(&pin_PB00) },

    { MP_ROM_QSTR(MP_QSTR_NeoPWR), MP_ROM_PTR(&pin_PB02) },
   
    { MP_ROM_QSTR(MP_QSTR_NEOPIXEL), MP_ROM_PTR(&pin_PB03) },

    { MP_ROM_QSTR(MP_QSTR_HVmeasurementAnalogIn), MP_ROM_PTR(&pin_PB08) },

    { MP_ROM_QSTR(MP_QSTR_A2), MP_ROM_PTR(&pin_PB09) },

    { MP_ROM_QSTR(MP_QSTR_BoostEnableOut), MP_ROM_PTR(&pin_PB13) },
    
    { MP_ROM_QSTR(MP_QSTR_TXD5), MP_ROM_PTR(&pin_PB16) },

    { MP_ROM_QSTR(MP_QSTR_RXD6), MP_ROM_PTR(&pin_PB17) },

    { MP_ROM_QSTR(MP_QSTR_MISO), MP_ROM_PTR(&pin_PB22) },
 
    { MP_ROM_QSTR(MP_QSTR_MOSI), MP_ROM_PTR(&pin_PB23) },

    { MP_ROM_QSTR(MP_QSTR_CANTX), MP_ROM_PTR(&pin_PB14) },
    { MP_ROM_QSTR(MP_QSTR_CANRX), MP_ROM_PTR(&pin_PB15) },
    { MP_ROM_QSTR(MP_QSTR_CANS), MP_ROM_PTR(&pin_PB12) },


    { MP_ROM_QSTR(MP_QSTR_I2C), MP_ROM_PTR(&board_i2c_obj) },
    { MP_ROM_QSTR(MP_QSTR_SPI), MP_ROM_PTR(&board_spi_obj) },
    { MP_ROM_QSTR(MP_QSTR_UART), MP_ROM_PTR(&board_uart_obj) },
};
MP_DEFINE_CONST_DICT(board_module_globals, board_module_globals_table);