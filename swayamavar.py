""" Swayamvar """
import random
import pandas


contestant_score = [0 for _ in range(500)]
contestant_id = [i for i in range(500)]
data_frame = pandas.DataFrame(
    {
        'id': contestant_id,
        'round_one_score': contestant_score,
        'round_two_score': contestant_score,
        'round_three_score': contestant_score,
        'total_score': contestant_score
    })

''' Round 1 '''
for ind in data_frame.index:
    family_bg_and_personal_profile_score = random.randint(65, 100)
    business_aptitude = random.randint(65, 100)
    value_system_score = random.randint(65, 100)
    if family_bg_and_personal_profile_score >= 75 and business_aptitude >= 75 \
            and value_system_score >= 75:
        avg_score = (family_bg_and_personal_profile_score +
                     business_aptitude + value_system_score)//3
        if avg_score > 85:
            data_frame['round_one_score'][ind] = avg_score
    data_frame['total_score'][ind] += data_frame['round_one_score'][ind]
data_frame.sort_values(['total_score'], axis=0,
                       ascending=False, inplace=True)
# top 100
data_frame = data_frame[:100]

''' Round 2 '''
for ind in data_frame.index:
    personality = random.randint(65, 100)
    values_and_empathy = random.randint(65, 100)
    business_and_family = random.randint(65, 100)
    if personality >= 75 and values_and_empathy >= 75 and \
            business_and_family >= 75:
        avg_score = (personality+values_and_empathy+business_and_family)//3
        if avg_score >= 85:
            data_frame['round_two_score'][ind] = avg_score
    data_frame['total_score'][ind] += data_frame['round_two_score'][ind]
data_frame.sort_values(['total_score'], axis=0,
                       ascending=False, inplace=True)
# top 10
data_frame = data_frame[:10]

''' Round 3 '''
for ind in data_frame.index:
    parents_score = random.randint(0, 20)
    siblings_score = random.randint(0, 20)
    rahuls_score = random.randint(0, 60)
    data_frame['round_three_score'][ind] = parents_score + \
        siblings_score + rahuls_score
    data_frame['total_score'][ind] += data_frame['round_three_score'][ind]
data_frame.sort_values(['total_score'], axis=0,
                       ascending=False, inplace=True)
# top 3
data_frame = data_frame[:3]

# winner selection
rahuls_option = [ind for ind in data_frame.index]
rahuls_choice = random.choice(rahuls_option)
print('Rahuls choice is contestant number: ', rahuls_choice)
