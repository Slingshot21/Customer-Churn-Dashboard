kpi1, kpi2, kpi3 = st.column(3) #create 3 placeholders

if uploaded_file is not None:

    aov = np.mean(df['Total Sales'])
    aov_goal = 95.00
    kpi1.metric(
        #label the metric
        label = 'AOV',
        #calculation
        value = f"${round(aov,2)}",
        #calculate the change compared to the goal
        delta = f"-${round(aov_goal,2)}" if aov_goal>aov else f"${round(aov-aov_goal,2)}"
    )

    nc = np.mean(df.loc[df['customer_type']== 'First-Time'].groupby(['day']).count()['customerid'])
    nc_goal = 30
    kpi2.metric(
        label = 'New Customers/Day',
        value = int(nc),
        delta = f"-{round(nc_goal-nc)/nc_goal*100,2}%" if nc_goal>nc else f"{round(nc- nc_goal)/ nc_goal*100,0}%",
    )

    rc = np.mean(df.loc[df['customer_type'] == "returning"].groupby['day'].count()['customerid'])\
    rc_goal = 250
    kpi3.metric(
        label = "Returning customers/day",
        value = int(rc),
        delta = f"-{round(rc_goal - rc)/rc_goal*100,2}%" if rc_goal>rc else f"{round((rc-rc_goal)/rc_goal*100,2)}%"
    )

    