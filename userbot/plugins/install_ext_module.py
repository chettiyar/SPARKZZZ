from userbot import bot
from telethon import events
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from userbot.utils import command, remove_plugin, load_module
from pathlib import Path
from userbot.utils import admin_cmd
import sys
import asyncio
import traceback
import os

@sparkzzz.on(admin_cmd(pattern=r"extdl$"))
async def install(event):
	if event.fwd_from:
		return
	documentss = await event.client.get_messages(event.chat_id, None ,search='.py', filter=InputMessagesFilterDocument)
	total = int(documentss.total)
	total_doxx = range(0, total)
	b = await event.client.send_message(event.chat_id, f"**Installing {total} plugins...**\n`This msg will be deleted after the installation gets completed`")
	text =  "**Installing New Plugins...**\n\n"
	a = await event.client.send_message(event.chat_id, text)
	if total == 0:
		await a.edit("**No plugins to install.**")
		await event.delete()
		return
	for ixo in total_doxx:
		mxo = documentss[ixo].id
		downloaded_file_name = await event.client.download_media(await event.client.get_messages(event.chat_id, ids=mxo), "userbot/plugins/")
		if "(" not in downloaded_file_name:
			path1 = Path(downloaded_file_name)
			shortname = path1.stem
			try:
				load_module(shortname.replace(".py", ""))
				text += f"**• Installed** `{(os.path.basename(downloaded_file_name))}` **successfully.**\n"
			except:
				text += f"**• Error installing** `{(os.path.basename(downloaded_file_name))}`\n"
		else:
			text += f"**• Plugin** `{(os.path.basename(downloaded_file_name))}` **already installed.**\n"
		await a.edit(f"{text}\n**Succesfully Installed all plugin.**")
		await event.delete()
		await b.delete()
