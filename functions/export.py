from pandas import ExcelWriter

def export(df, data_name):
    fname = '/home/bi-ebm/Instagram-Scraper/DADOS/' + data_name + '.xlsx'

    writer = ExcelWriter(fname)
    df.to_excel(writer, 'comentários', index=False)
    writer.save()
