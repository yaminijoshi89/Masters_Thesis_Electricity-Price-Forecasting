#%%
from entsoe import EntsoeRawClient,EntsoePandasClient
import pandas as pd
client_pd = EntsoePandasClient(api_key='9a9df453-dc5d-40a7-8400-1c2f6bd53d9b')
#client = EntsoeRawClient(api_key='9a9df453-dc5d-40a7-8400-1c2f6bd53d9b')
#DE_TENNET =     '10YDE-EON------1', 'TenneT GER CA',                                'Europe/Berlin',
#DE_TRANSNET =   '10YDE-ENBW-----N', 'TransnetBW CA',                                'Europe/Berlin',
#DE_AT_LU =      '10Y1001A1001A63L', 'DE-AT-LU BZ',                                  'Europe/Berlin',
#DE_LU =         '10Y1001A1001A82H', 'DE-LU BZ / MBA',                               'Europe/Berlin',
#DE_AMP_LU =     '10Y1001C--00002H', 'Amprion LU CA',                                'Europe/Berlin'
#DE =            '10Y1001A1001A83F', 'Germany',                                      'Europe/Berlin'
#CZ_DE_SK =      '10YDOM-CZ-DE-SKK', 'BZ CZ+DE+SK BZ / BZA',                         'Europe/Prague',
#DE_50HZ =       '10YDE-VE-------2', '50Hertz CA, DE(50HzT) BZA',                    'Europe/Berlin',
#DE_AMPRION =    '10YDE-RWENET---I', 'Amprion CA',                                   'Europe/Berlin',
start_arc = pd.Timestamp('20171201', tz='Europe/Brussels')
end_arc = pd.Timestamp('20190101', tz='Europe/Brussels')
start = pd.Timestamp('20190101', tz='Europe/Brussels')
end = pd.Timestamp('20231230', tz='Europe/Brussels')
country_code = 'BE'  # Belgium
country_code_from = 'FR'  # France
country_code_to = 'DE_LU' # Germany-Luxembourg
type_marketagreement_type = 'A01'
contract_marketagreement_type = 'A01'
process_type = 'A51'
#client_pd.query_day_ahead_prices("DE_AT_LU", start=start, end=end)
#%%
df_de_at_lu = client_pd.query_day_ahead_prices("DE_AT_LU", start=start_arc, end=end_arc)
#%%
df_de_lu = client_pd.query_day_ahead_prices("DE_LU", start=start, end=end)
#%%
df_de_amprion = client_pd.query_day_ahead_prices("DE_AMPRION", start=start, end=end)
#%%
df_de_50hz = client_pd.query_day_ahead_prices("DE_50HZ", start=start, end=end)
#%%
df_de_amp_lu = client_pd.query_day_ahead_prices("DE_AMP_LU", start=start, end=end)
#%%
df_de_lu.to_csv("de_lu_2019-23.csv")
df_de_at_lu.to_csv("de_at_lu_2017-19.csv")
#%%
import matplotlib.pyplot as plt
pd_de_lu = pd.DataFrame(df_de_lu,   columns=['price'])
pd_de_at_lu = pd.DataFrame(df_de_at_lu,   columns=['price'])
plt.plot(pd_de_at_lu.index,pd_de_at_lu.price)
#%%
plt.plot(pd_de_at_lu.index,pd_de_at_lu.price)
plt.title("Time Series of price Changes Over 2017-2019")
plt.xlabel("Time (hour)")
plt.ylabel("Day-ahead Price")
plt.grid(True)
plt.show()

#%%
plt.plot(pd_de_lu.index,pd_de_lu.price)
plt.title("Time Series of price Changes Over 2019-2023")
plt.xlabel("Time (hour)")
plt.ylabel("Day-ahead Price")
plt.grid(True)
plt.show()
#%%
pd_de_lu.resample("Y")
