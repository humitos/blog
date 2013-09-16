from nikola.plugins.command.import_wordpress import CommandImportWordpress, get_text_tag

ciw = CommandImportWordpress
channel = ciw.get_channel_from_file('/media/humitos/8c9aa144-b4eb-4c05-8ecb-3e6cb2213ef5/descargas/home-humitos-backup/Downloads/humitos.wordpress.2013-09-09.xml')


for item in channel.findall('item'):
    wordpress_namespace = item.nsmap['wp']
    post_type = get_text_tag(
            item, '{{{0}}}post_type'.format(wordpress_namespace), 'post')
    if post_type == 'attachment':
        post_id = get_text_tag(item, '{{{0}}}post_id'.format(wordpress_namespace), 'NO ID')
        attachment_url = get_text_tag(item, '{{{0}}}attachment_url'.format(wordpress_namespace), 'NO ID')
        print post_id, attachment_url

