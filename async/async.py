import asyncio

async def clean(places):
    await asyncio.sleep(3)
    not_s = 0
    if type(places) == list:
        for place in places:
            if type(place) == str:
                pass
            else:
                els = 1
        if not_s == 0:
            for each in places:
                print(f'{each} cleaned!', end = ' | ')
        else:
            print('inputs types must be str!!!')
    else:
        print('No list entered!!')

async def invite(people):
    await asyncio.sleep(2)
    not_s = 0
    if type(people) == list:
        for person in people:
            if type(person) == str:
                pass
            else:
                not_s = 1
        if not_s == 0:
            for person in people:
                print(f'{person} invited!', end = ' | ')
        else:
            print('wrong input type. must be str!!!!')
    else:
        print('input must be a list!!!!')

async def run_funcs(funcs_list, args):
    if type(funcs_list) == list:
        if type(args) == list:
            clean_task = asyncio.create_task(funcs_list[0](args[0]))
            invite_task = asyncio.create_task(funcs_list[1](args[1]))
            await clean_task
            await invite_task
    else:
        print('inputs must be a list!!!')
        
async def main():
    await run_funcs([clean, invite], [['yard', 'back yard', 'floor', 'balconi', 'bed room'], ['ali', 'alex', 'ellen', 'alexander']])

asyncio.run(main())