# =============================================================================
# ENGR 1210 - Morse Optical Comms
# =============================================================================
# GOAL
#   Blink a Morse message on an LED - first on your LAPTOP, then, with the SAME
#   file and no changes, on a real Pico 2 in Wokwi. That "it just works on the
#   board too" moment is the whole idea of a HAL (Hardware Abstraction Layer).
#
# =============================================================================

import hal_pc as hw
#import hal_pico as hw  # uncomment this line to run on the real Pico 2
from morse_code import WORD_GAP_MS, DOT_MS, DASH_MS, SYMBOL_GAP_MS, LETTER_GAP_MS, encode_message




def blink_word(message):
    for pattern in encode_message(message):      
        if pattern == ' ':
            hw.set_led_timed(False, WORD_GAP_MS)
        else:
            for symbol in pattern:
                if symbol == '.':
                    hw.set_led_timed(True, DOT_MS)
                elif symbol == '-':
                    hw.set_led_timed(True, DASH_MS)
                hw.set_led_timed(False, SYMBOL_GAP_MS)
            hw.set_led_timed(False, LETTER_GAP_MS)
    print("...done")

print("Board:", hw.board_info())
print("Type a message and watch it blink. Type 'quit' to stop.")

while True:
    message = input("\nWord to blink in morse (or 'quit'): ").strip()
    if message.lower() == "quit":
        break
    if message:
        blink_word(message)