import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer

class WorkerRushBot(sc2.BotAI):
    async def on_step(self, iteration):
        # Build Supply Depots as needed until you have 16 or 18 supply
        if self.supply_left < 2 and not self.already_pending(SUPPLY_DEPOT):
            if self.can_afford(SUPPLY_DEPOT):
                await self.build(SUPPLY_DEPOT, near=self.main_base_ramp.barracks_correct_placement)

        # Build SCVs as quickly as possible
        if self.units(SCV).amount < 30 and self.can_afford(SCV) and self.supply_left > 0:
            await self.do(self.units(COMMAND_CENTER).first.train(SCV))

        # Attack with all of your SCVs when you have a sufficient number
        if self.units(SCV).amount > 15:
            target = self.known_enemy_structures.random_or(self.enemy_start_locations[0]).position
            for scv in self.units(SCV).idle:
                await self.do(scv.attack(target))

run_game(maps.get("(2)RedshiftLE"), [
    Bot(Race.Terran, WorkerRushBot()),
    Computer(Race.Terran, Difficulty.Easy)
], realtime=True)