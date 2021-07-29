from pandas import ExcelWriter

def export(df, name_data):
    fname = '/home/bi-ebm/Instagram-Scraper/DADOS/' + name_data + '.xlsx'

    writer = ExcelWriter(fname)
    df.to_excel(writer, 'comentários', index=False)
    writer.save()
