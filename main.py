import discord
import discord.ext.commands
import json
import os
from looper import loop

Token = os.environ['Token']
commands = discord.ext.commands
client = commands.Bot(command_prefix = "!pd ")

error_message = discord.Embed(title = "Something went wrong", color = discord.Color.red(), description = "uh-oh, Something went wrong, please check your commands with `!pd help commands`")
jobBoard = discord.Embed(title="Jobs for the Jobless created by GrunkGrunk")

jobBoard.add_field(name = "Traveling Merchant",value = "Earns 500 per week by selling various items and trinkets all around the country of Valoria. (Requirement: Buy A Wagon.)",inline = False)

jobBoard.add_field(name = "Military Soldier",value = """**Events are not automatic**
Earns 100-5000 per week depending on your rank, if you are just a guard in the commons you'll only earn a small pay for protecting the town. But if you guard the royal family, of course you will be paid handsomely because, you're protecting their life. (Requirement: Apply At A Barracks Or Event.)""", inline = False)

jobBoard.add_field(name = "Shop Owner",value = "Earns pay by selling the items they sell. Has a small to big store with items and weapons and anything imaginable for the sole person of selling for more money. (Requirement: Buy A Building and Turn It Into A Shop.)", inline = False)

jobBoard.add_field(name = "Fisher",value =" Earns pay based on the fish they catch. Fishes by the piers at the edges of Valoria.(Requirement: Buy A Fishing Rod and Fishing License.)", inline = False)

HelpPage = discord.Embed(title = "Help Page", description = "A nice wonderfull help page for your needs")
HelpPage.add_field(name = "Commands", value = "All the commands on pocket dimension", inline = False)
HelpPage.add_field(name = "Farming",value =  "Quick Guide to farming")
HelpCommands = discord.Embed(title = "Commands", description = """All commands must start with !pd

Help
- The help page

Profile
- Your Profile

Jobs
- All Jobs available in PocketDimension



 **This list is subject to change.**""")


@client.event
async def on_ready():
  print("Init...")
  print("Initializing")


@client.command()
async def jobs(ctx):
  await ctx.send(embed = jobBoard)

@client.command()
async def Help(ctx, arg):
  if arg == None:
    await ctx.send(embed = HelpPage)
  elif arg == "commands":
    await ctx.send(embed = HelpCommands)
  else:
    await ctx.send(embed = error_message)
    return

@client.command(aliases = ["Inventory","profile","Inv","inv","p"])
async def Profile(ctx):
  await new_account(ctx.author)
  user = ctx.author
  users = await get_bank()
  inv_data = [users[str(user.id)]["pocket"],users[str(user.id)]["bank"],users[str(user.id)]["plots"],users[str(user.id)]["T1 Crops"],users[str(user.id)]["T2 Crops"],users[str(user.id)]["T3 Crops"],]

  inv = discord.Embed(title =  f"{ctx.author}'s Profile", color = discord.Color.green())
  inv.add_field(name = "Pocket Money", value = inv_data[0])
  inv.add_field(name = "Bank Account", value = inv_data[1])
  inv.add_field(name = "Plots", value = inv_data[2])
  inv.add_field(name = "Tier 1 Crops", value = inv_data[3], inline = True)
  inv.add_field(name = "Tier 2 Crops", value = inv_data[4], inline = True)
  inv.add_field(name = "Tier 3 Crops", value = inv_data[5], inline = True)
  await ctx.send(embed = inv)


@client.command(aliases = ["work"])
async def collect(ctx):
  await ctx.send(embed = error_message)
  return

async def new_account(user):
  users = await get_bank()
  with open("data.json", "r") as f:
    users = json.load(f)
  if str(user.id) in users:
      return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["pocket"] = 0
    users[str(user.id)]["bank"] = 0
    users[str(user.id)]["plots"] = 0
    users[str(user.id)]["T1 Crops"] = 0
    users[str(user.id)]["T2 Crops"] = 0
    users[str(user.id)]["T3 Crops"] = 0
    users[str(user.id)]["Fish"] = 0
    users[str(user.id)]["Rare Fish"] = 0
  with open("data.json", "w") as f:
    json.dump(users,f)
    return True


async def get_bank():
  with open("data.json", "r") as f:
    users = json.load(f)
  return users

loop()
client.run(Token)