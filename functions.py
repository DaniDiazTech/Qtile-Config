from libqtile.command import lazy

class Functions(object):
    
    ##### MOVE WINDOW IN GROUPS #####
	@staticmethod
	def window_to_prev_group():
		@lazy.function
		def __inner(qtile):
			i = qtile.groups.index(qtile.current_group)

			if qtile.current_window and i != 0:
				group = qtile.groups[i - 1].name
				qtile.current_window.togroup(group, switch_group=True)
		return __inner

	@staticmethod
	def window_to_next_group():
		@lazy.function
		def __inner(qtile):
			i = qtile.groups.index(qtile.current_group)

			if qtile.current_window and i != len(qtile.groups):
				group = qtile.groups[i + 1].name
				qtile.current_window.togroup(group, switch_group=True)
		return __inner


    	##### KILL ALL WINDOWS #####

	@staticmethod
	def kill_all_windows():
		@lazy.function
		def __inner(qtile):
			for window in qtile.current_group.windows:
				window.kill()
		return __inner

	@staticmethod
	def kill_all_windows_minus_current():
		@lazy.function
		def __inner(qtile):
			for window in qtile.current_group.windows:
				if window != qtile.current_window:
					window.kill()
		return __inner


if __name__ == "__main__":
    pass
