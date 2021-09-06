from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/884318606672941067/VrL-e2TYFwKy4NBm5FAzYPx4ClLFlNkNn9VB708txqKbyKANj0GjbwlqSS-va06gd4Uo', username="JUICE")

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