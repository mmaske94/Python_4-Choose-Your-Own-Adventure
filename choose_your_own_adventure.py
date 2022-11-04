name = input('Type Your Name: ')
print('Welcome',name, 'to Choose Your Own Adventure')

answer1 = input('You Are On A Dirt Road. You can go either left or right. Which Way Would You Like To Go? ').lower()

if answer1 == 'left':
    answer2 = input('You Come To A River, You can either walk on the bridge over it or swim under the bridge. Write either Walk or Swim: ').lower()

    if answer2 == 'swim':
        print('An Alligator Came Across Your Path. You Loose')
    elif answer2 == 'walk':
        print('Death met you on the bridge, you loose')
    else:
         print('Not a valid answer, you loose')
elif answer1 == 'right':
    answer2 = input('You Meet an Ogre, do you want to Fight or Run? ').lower()

    if answer2 == 'fight':
        print('You Won! And You Won a pot of gold!')
    elif answer2 == 'run':
        print('You ran into a troll. You lost')
    else:
        print('Not a valid answer, you loose')
else:
    print('Not a valid answer, you loose')
