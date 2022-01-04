const discord = require('discord.js');
const client = new discord.Client();
client.login('ODAzNjE2MjY0NjM0NzYxMjM4.YBAX9w.XcGJocNrRc3jjSLejC8Gxjo8gps');
client.on('ready', () => {
console.log('The bot is ready');
 
});

client.on('message', message => {
    if (message.author.bot) return;

    if (message.content.toLowerCase() === '?embed' )
    {
      const embed = new discord.MessageEmbed();
      // you can change below for different embed //
      embed.setAuthor(client.user.username, client.user.displayAvatarURL);
      embed.setDescription("----------------------------------------------------------------------------");
      embed.addField("Rules", "Any Sort Of Staff Disrespect Will Result in a: Warn/Mute/Ban");
      embed.addField("•Advertising", " isn't allowed anywhere except #media");
      embed.addField("Be nice.", "Be respectful of other people in our server. especially to staff");
      embed.addField("•Topics.", "Please keep your topics in the correct channel");
      embed.addField("Ranks" , "Don't ask for higher ranks, apply for them.");
      embed.addField("Material", "Sending/Linking any harmful material such as viruses, IP grabbers, results in an immediate and permanent ban.");
      embed.addField("Mute warning", "Being disrespectful/mean in a VC, will get you server muted.");
      embed.setColor("YELLOW")
      embed.setFooter("-------------------------------------------------------------------------------");
      embed.setThumbnail("https://cdn.abcotvs.com/dip/images/4385330_Rules1280.jpg?w=1280&r=16%3A9");
      // you can change the above for different embed //
      message.channel.send({embed});
    }
});