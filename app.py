
# %%
import pandas as pd
import streamlit as st
import altair as alt

results = pd.read_csv('~/Documents/personal/rusa/data/event_results.csv')
# %%
#results['finish_hours'] = results['hours'] + (results['minutes'] / 60)
# %%
arvi_events = results[results['rusa'] == 11548].eid
which_event = st.selectbox(
    'Choose an Event ID', arvi_events)
# %%
chart_data = results[results['eid'] == which_event]
chart_obj = alt.Chart(chart_data).mark_bar().encode(x = 'hours', y = 'count()')

# %%
st.write(f'Finish times by hour bucket for event {which_event}')
st.altair_chart(chart_obj)

st.write('Total finishers %s' % chart_data.shape[0])