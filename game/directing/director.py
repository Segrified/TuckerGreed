class Director:

    def __init__(self, keyboard_service, video_service, score):
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.score = score
        
    #Starts and loops the game until the window is closed
    def start_game(self, cast):
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    #Checks inputs
    def _get_inputs(self, cast):
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    #Updates the gamestate
    def _do_updates(self, cast):
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("gems")
        artifacts += cast.get_actors("rocks")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                if artifact._text == "*":
                    self.score.updateScore(1)
                    cast.remove_actor("gems", artifact)
                if artifact._text == "O":
                    self.score.updateScore(-1)
                    cast.remove_actor("rocks", artifact)

            artifact.move_next(max_x, max_y)
        
    #Aplies the outputs
    def _do_outputs(self, cast):
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self.score.drawScore()
        self._video_service.flush_buffer()
        
