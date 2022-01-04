const Discord = require('discord.js');
const { Intents } = require('discord.js');
const client = new Discord.Client();
const TOKEN = "ODAzNjE2MjY0NjM0NzYxMjM4.YBAX9w.XcGJocNrRc3jjSLejC8Gxjo8gps"
client.on('ready', () => {
console.log(`Logged in as ${client.user.tag}`);
});

client.login(TOKEN)