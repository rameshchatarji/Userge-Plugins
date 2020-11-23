# by Alone

import asyncio

from userge import userge, Message

@userge.on_cmd("muth$", about={'header': "Mukamaituna"})
async def muth_func(message):
  animation_chars = [          
            "8✊️===D",
            "8=✊️==D",
            "8==✊️=D",
            "8===✊️D",
            "8==✊️=D",
            "8=✊️==D",
            "8✊️===D",
            "8=✊️==D",
            "8==✊️=D",
            "8===✊️D",
            "8===✊️D💦",
            "8==✊️=D💦💦",
            "8=✊️==D💦💦💦"
          ]
  for i in range(13):
    await asyncio.sleep(0.3)
    await message.edit(animation_chars[i % 13])