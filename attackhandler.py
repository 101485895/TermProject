import random
class AttackHandler:
    # Physical/General Attacks
    @staticmethod
    def slash(combat_strength):
        # Basic attack with very low variance
        return round(combat_strength + random.randint(-1, 1))

    @staticmethod
    def cleave(combat_strength):
        # Basic attack with slightly more variance for more risk/reward
        return round(combat_strength + random.randint(-2, 3))

    @staticmethod
    def body_slam(combat_strength):
        # Absolutely no variance on damage
        return round(combat_strength * 1.1)

    #=============================================================
    #Fire Spells - Generic Attacking Spells
    @staticmethod
    def fire_ball(combat_strength):
        # Deals greater damage but with greater variance
        return round((combat_strength * 1.5) + random.randint(-4, 4))

    @staticmethod
    def fire_whip(combat_strength):
        # Deals slightly more damage but with slightly less variance
        return round((combat_strength * 1.3) + random.randint(-1, 3))

    @staticmethod
    def fire_storm(combat_strength):
        # Slightly weaker fireball with more variance
        return round((combat_strength * 1.4) + random.randint(-6, 6))

    @staticmethod
    def fire_spark(combat_strength):
        # Low base damage but cannot roll less damage, resulting in a floor of damage
        return round((combat_strength * 0.8) + random.randint(0, 2))

    @staticmethod
    def fire_blast(combat_strength):
        # High base damage, but only can only roll negative
        return round((combat_strength * 2.0) + random.randint(-8, 0))

    #=============================================================
    #Water Spells - Generally Weaker, but contains defensive spell
    @staticmethod
    def water_bolt(combat_strength):
        # Weaker spell, can roll a bit lower
        return round((combat_strength * 1.2) + random.randint(-3, 1))

    @staticmethod
    def water_surge(combat_strength):
        # Similar to bolt with higher base and greater variance
        return round((combat_strength * 1.4) + random.randint(-4, 2))

    @staticmethod
    def water_shield(combat_strength):
        # Unique spell that helps reduce damage scaling off of your strength
        return -round(combat_strength * 0.5)

    @staticmethod
    def water_tide(combat_strength):
        # Very weak but only can roll up
        return round((combat_strength * 0.8) + random.randint(1, 6))

    @staticmethod
    def water_crash(combat_strength):
        # Stronger base, but always rolls lower
        return round((combat_strength * 1.7) + random.randint(-6, -1))

    #=============================================================
    #Lightning Spells - Very High Risk/Reward spells
    @staticmethod
    def lightning_strike(combat_strength):
        # High base with very high variance
        return round((combat_strength * 1.8) + random.randint(-10, 10))

    @staticmethod
    def lightning_chain(combat_strength):
        # Lower base with favor towards rolling up
        return round((combat_strength * 1.1) + random.randint(-3, 6))

    @staticmethod
    def lightning_jolt(combat_strength):
        # Very weak but only  can roll up
        return round((combat_strength * 0.8) + random.randint(1, 6))

    @staticmethod
    def lightning_clash(combat_strength):
        # Highest variance spell, can go as low as 0 dmg (pretty much failed the spell)
        return round(combat_strength * random.uniform(0, 4))

    @staticmethod
    def lightning_overload(combat_strength):
        # High base damage but can only roll low
        return round((combat_strength * 3.0) + random.randint(-12, 0))

    #=============================================================
    #Monster Attacks
    @staticmethod
    def strike(combat_strength):
        # Basic attack with very low variance
        return round(combat_strength + random.randint(-1, 1))

    @staticmethod
    def double_slash(combat_strength):
        # Two weaker hits to balance out to deal decent damage
        return round(2 *((combat_strength * 0.6) + random.randint(-2, 2)))

    @staticmethod
    def power_strike(combat_strength):
        # Stronger hit
        return round((combat_strength * 1.5) + random.randint(1, 4))

    @staticmethod
    def desperate_lunge(combat_strength):
        # Stronger hit but with great variance
        return round((combat_strength * 1.7) + random.randint(-4, 6))

    @staticmethod
    def death_blow(combat_strength):
        # Critical hit mechanic, 9 and 10 result in a critical hit which does 1.5x more damage.
        crit_check = random.randint(1,10)
        if crit_check >= 9:
            return round(1.5*((combat_strength * 2) + random.randint(-6, 8)))
        else:
            return round((combat_strength * 2) + random.randint(-6, 8))

    @staticmethod
    def last_stand(combat_strength):
        # Very similar to lightning crash which randoms the entire attack with very high risk/reward
        return round(combat_strength * random.uniform(0, 4.5))

    @classmethod
    def handle(cls, attack_name, combat_strength):
        method_name = attack_name.lower().replace(' ', '_') # Converts selected option into valid function name (Fire Ball > fire_ball)
        return getattr(cls, method_name)(combat_strength) # Calls respective function based on selected attack