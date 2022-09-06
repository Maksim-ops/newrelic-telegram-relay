#!/bin/bash
sed -i -e "s/%CHAT_ID%/$CHAT_ID/g" -e "s/%BOT_TOKEN%/$BOT_TOKEN/g" ./config/telegram.json && python ./main.py
