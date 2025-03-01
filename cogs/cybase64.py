from discord.ext import commands
import base64
import discord
from discord import app_commands

from utils.util import create_codeblock


class CYbase64(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="cybase64", description="y談用のBase64変換です")
    @app_commands.describe(text="送信したい内容を書いてください")
    async def cybase64(self, interaction: discord.Interaction, text: str):
        send_channel = await self.bot.fetch_channel(892062687557738548)
        admin_channel = await self.bot.fetch_channel(1213498919145963551)
        yembed = discord.Embed(
            color=0xd51ebe,
            title=interaction.user.display_name,
            description=create_codeblock(base64.b64encode(text.encode()).decode()),
        )
        admin_embed = discord.Embed(
            color=0xd51ebe,
            title=interaction.user.display_name,
            description=f"y談送信内容\n{text}"
        )
        if interaction.channel == send_channel:
            await interaction.response.send_message("送信しました", ephemeral=True)
            await send_channel.send(embed=yembed)
            await admin_channel.send(embed=admin_embed)
        else:
            await interaction.response.send_message("チャンネル違うよ！", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(CYbase64(bot))
