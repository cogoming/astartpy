class GameStats:
    def __init__(self,ai_settings):
        """跟踪游戏的统计信息"""
        self.ai_settings = ai_settings
        self.reset_starts()
        # 游戏刚启动时处于活动状态
        self.game_active = False
    def reset_starts(self):
        self.ships_left = self.ai_settings.ship_limit

