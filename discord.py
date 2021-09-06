from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url='ENTER WEBHOOK URL HERE', username="JUICE")

def send_hook(product_title, url, price, sku, imageURL, direct_link):
    embed = DiscordEmbed(title = product_title, description='PRODUCT AVAILABLE', color='03b2f8')
    embed.set_author(name='Monitors by JUICE', url=url)
    embed.set_timestamp()
    embed.add_embed_field(name='Price', value=price)
    embed.add_embed_field(name='SKU', value=sku)
    embed.set_thumbnail(url=imageURL)
    embed.add_embed_field(name='Add To Cart', value=direct_link)
    

    webhook.add_embed(embed)
    response = webhook.execute()