from Character import Character
class Monster(Character):
    def __init__(self):
        super().__init__()
    
    def monster_attacks(m_combat_strength, health_points):
        ascii_image2 = """                                                                 
            @@@@ @                           
        (     @*&@  ,                         
        @               %                       
        &#(@(@%@@@@@*   /                      
        @@@@@.                                
                @       /                    
                    %         @                 
                ,(@(*/           %              
                @ (  .@#                 @   
                            @           .@@. @
                    @         ,              
                        @       @ .@          
                                @              
                            *(*  *      
                """
        print(ascii_image2)
        print("    |    Monster's Claw (" + str(m_combat_strength) + ") ---> Player (" + str(health_points) + ")")
        if m_combat_strength >= health_points:
            # Monster was strong enough to kill player in one blow
            health_points = 0
            print("    |    Player is dead")
        else:
            # Monster only damaged the player
            health_points -= m_combat_strength
            print("    |    The monster has reduced Player's health to: " + str(health_points))
        return health_points
    
    def __del__(self):
        print("Monster object taken by garbage collector")
        super().__del__()