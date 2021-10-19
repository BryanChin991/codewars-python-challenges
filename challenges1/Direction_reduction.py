opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    print(new_plan)

    # plan = ' '.join(plan)
    # while True:
    #     old = plan
    #     plan = plan.strip()
    #     plan = plan.replace('NORTH SOUTH ', '')
    #     plan = plan.replace('SOUTH NORTH ', '')
    #     plan = plan.replace('EAST WEST ', '')
    #     plan = plan.replace('WEST EAST ', '')
    #
    #     if plan == old:
    #         print(plan.split())
    #         break


dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
dirReduc(["NORTH", "EAST", "SOUTH", "WEST"])
dirReduc(["NORTH", "EAST", "SOUTH", "WEST", 'EAST', 'NORTH', 'SOUTH'])