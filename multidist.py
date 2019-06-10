def multidist(data, rows, columns, width, length, label):
    """
    Must import Seaborn and matplotlib.pyplot.
    Purpose of this module is for convenience of plotting multiple windows distribution without many lines of the code on jupyter notebook.
    """
    f, axes = plt.subplots(rows, columns, figsize=(width, length))

    for names in data.columns:
        

    sns.distplot(position1['won'], hist=False, color='blue', kde_kws={'shade': True}, ax=axes[0, 0], label='1st')
    sns.distplot(position2['won'], hist=False, color='red', kde_kws={'shade': True}, ax=axes[0, 0], label='2nd')
    sns.distplot(position3['won'], hist=False, color='yellow', kde_kws={'shade': True}, ax=axes[0, 0],label='3rd')
    sns.distplot(position4['won'], hist=False, color='green', kde_kws={'shade': True}, ax=axes[0, 0],label='4th')

    sns.distplot(position1['lost'], hist=False, color='blue', kde_kws={'shade': True}, ax=axes[0, 1],label='1st')
    sns.distplot(position2['lost'], hist=False, color='red', kde_kws={'shade': True}, ax=axes[0, 1], label='2nd')
    sns.distplot(position3['lost'], hist=False, color='yellow', kde_kws={'shade': True}, ax=axes[0, 1], label='3rd')
    sns.distplot(position4['lost'], hist=False, color='green', kde_kws={'shade': True}, ax=axes[0, 1], label='4th')

    sns.distplot(position1['drawn'], hist=False, color='blue', kde_kws={'shade': True}, ax=axes[0, 2],label='1st')
    sns.distplot(position2['drawn'], hist=False, color='red', kde_kws={'shade': True}, ax=axes[0, 2], label='2nd')
    sns.distplot(position3['drawn'], hist=False, color='yellow', kde_kws={'shade': True}, ax=axes[0, 2], label='3rd')
    sns.distplot(position4['drawn'], hist=False, color='green', kde_kws={'shade': True}, ax=axes[0, 2], label='4th')

    sns.distplot(position1['tackle_success'], hist=False, color='blue', kde_kws={'shade': True}, ax=axes[1, 0],label='1st')
    sns.distplot(position2['tackle_success'], hist=False, color='red', kde_kws={'shade': True}, ax=axes[1, 0], label='2nd')
    sns.distplot(position3['tackle_success'], hist=False, color='yellow', kde_kws={'shade': True}, ax=axes[1, 0], label='3rd')
    sns.distplot(position4['tackle_success'], hist=False, color='green', kde_kws={'shade': True}, ax=axes[1, 0], label='4th')

    sns.distplot(position1['clearance'], hist=False, color='blue', kde_kws={'shade': True}, ax=axes[1, 1],label='1st')
    sns.distplot(position2['clearance'], hist=False, color='red', kde_kws={'shade': True}, ax=axes[1, 1], label='2nd')
    sns.distplot(position3['clearance'], hist=False, color='yellow', kde_kws={'shade': True}, ax=axes[1, 1], label='3rd')
    sns.distplot(position4['clearance'], hist=False, color='green', kde_kws={'shade': True}, ax=axes[1, 1], label='4th')

    sns.distplot(position1['big_chance_created'], hist=False, color='blue', kde_kws={'shade': True}, ax=axes[1, 2],label='1st')
    sns.distplot(position2['big_chance_created'], hist=False, color='red', kde_kws={'shade': True}, ax=axes[1, 2], label='2nd')
    sns.distplot(position3['big_chance_created'], hist=False, color='yellow', kde_kws={'shade': True}, ax=axes[1, 2], label='3rd')
    sns.distplot(position4['big_chance_created'], hist=False, color='green', kde_kws={'shade': True}, ax=axes[1, 2], label='4th')

    sns.distplot(position1['aerial_battles'], hist=False, color='blue', kde_kws={'shade': True}, ax=axes[2, 0],label='1st')
    sns.distplot(position2['aerial_battles'], hist=False, color='red', kde_kws={'shade': True}, ax=axes[2, 0], label='2nd')
    sns.distplot(position3['aerial_battles'], hist=False, color='yellow', kde_kws={'shade': True}, ax=axes[2, 0], label='3rd')
    sns.distplot(position4['aerial_battles'], hist=False, color='green', kde_kws={'shade': True}, ax=axes[2, 0], label='4th')

    sns.distplot(position1['interceptions'], hist=False, color='blue', kde_kws={'shade': True}, ax=axes[2, 1],label='1st')
    sns.distplot(position2['interceptions'], hist=False, color='red', kde_kws={'shade': True}, ax=axes[2, 1], label='2nd')
    sns.distplot(position3['interceptions'], hist=False, color='yellow', kde_kws={'shade': True}, ax=axes[2, 1], label='3rd')
    sns.distplot(position4['interceptions'], hist=False, color='green', kde_kws={'shade': True}, ax=axes[2, 1], label='4th')