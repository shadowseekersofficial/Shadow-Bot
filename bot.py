2026-04-09T17:10:48.831868940Z [inf]  Starting Container
2026-04-09T17:10:49.784210514Z [err]  [2026-04-09 17:10:48] [INFO    ] discord.client: logging in using static token
2026-04-09T17:10:49.784214712Z [err]  [2026-04-09 17:10:49] [INFO    ] discord.gateway: Shard ID None has connected to Gateway (Session ID: a77e777075c68fcc978bf8f7ed57498a).
2026-04-09T17:10:51.787821726Z [inf]  [SHADOW BOT] Logged in as Shadowbot#8129 (1491660465489580032)
2026-04-09T17:10:52.134031959Z [inf]  [SHADOW BOT] Synced 9 slash commands
2026-04-09T17:10:54.852813209Z [inf]  [SHADOW BOT] Loaded 2 members from GAS
2026-04-09T17:10:54.852816831Z [inf]  [SHADOW BOT] Daily task scheduled at 23:55 Asia/Kolkata
2026-04-09T17:16:08.145628877Z [err]    File "/opt/venv/lib/python3.11/site-packages/discord/app_commands/commands.py", line 883, in _invoke_with_namespace
2026-04-09T17:16:08.145684200Z [err]  [2026-04-09 17:16:01] [ERROR   ] discord.app_commands.tree: Ignoring exception in command 'link'
2026-04-09T17:16:08.145689044Z [err]  Traceback (most recent call last):
2026-04-09T17:16:08.145694040Z [err]    File "/opt/venv/lib/python3.11/site-packages/discord/app_commands/commands.py", line 858, in _do_call
2026-04-09T17:16:08.145698981Z [err]      return await self._callback(interaction, **params)  # type: ignore
2026-04-09T17:16:08.145704055Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-04-09T17:16:08.145708187Z [err]    File "/app/bot.py", line 450, in link
2026-04-09T17:16:08.145712113Z [err]      await ch.send(embed=embed)
2026-04-09T17:16:08.145716953Z [err]    File "/opt/venv/lib/python3.11/site-packages/discord/abc.py", line 1618, in send
2026-04-09T17:16:08.145720015Z [err]      data = await state.http.send_message(channel.id, params=params)
2026-04-09T17:16:08.145723341Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-04-09T17:16:08.145726358Z [err]    File "/opt/venv/lib/python3.11/site-packages/discord/http.py", line 752, in request
2026-04-09T17:16:08.145729600Z [err]      raise Forbidden(response, data)
2026-04-09T17:16:08.145732657Z [err]  discord.errors.Forbidden: 403 Forbidden (error code: 50001): Missing Access
2026-04-09T17:16:08.145736260Z [err]  
2026-04-09T17:16:08.145739424Z [err]  The above exception was the direct cause of the following exception:
2026-04-09T17:16:08.145742425Z [err]  
2026-04-09T17:16:08.145745325Z [err]  Traceback (most recent call last):
2026-04-09T17:16:08.145748252Z [err]    File "/opt/venv/lib/python3.11/site-packages/discord/app_commands/tree.py", line 1310, in _call
2026-04-09T17:16:08.145751344Z [err]      await command._invoke_with_namespace(interaction, namespace)
2026-04-09T17:16:08.147091677Z [err]      return await self._do_call(interaction, transformed_values)
2026-04-09T17:16:08.147095162Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-04-09T17:16:08.147097959Z [err]    File "/opt/venv/lib/python3.11/site-packages/discord/app_commands/commands.py", line 876, in _do_call
2026-04-09T17:16:08.147101059Z [err]      raise CommandInvokeError(self, e) from e
2026-04-09T17:16:08.147104185Z [err]  discord.app_commands.errors.CommandInvokeError: Command 'link' raised an exception: Forbidden: 403 Forbidden (error code: 50001): Missing Access
2026-04-09T17:16:16.770276744Z [err]  
2026-04-09T17:16:16.770282714Z [err]    File "/app/bot.py", line 450, in link
2026-04-09T17:16:16.770283722Z [err]      await command._invoke_with_namespace(interaction, namespace)
2026-04-09T17:16:16.770288714Z [err]  Traceback (most recent call last):
2026-04-09T17:16:16.770295898Z [err]    File "/opt/venv/lib/python3.11/site-packages/discord/app_commands/commands.py", line 883, in _invoke_with_namespace
2026-04-09T17:16:16.770296091Z [err]      await ch.send(embed=embed)
2026-04-09T17:16:16.770297037Z [err]    File "/opt/venv/lib/python3.11/site-packages/discord/app_commands/tree.py", line 1310, in _call
2026-04-09T17:16:16.770299392Z [err]  [2026-04-09 17:16:16] [ERROR   ] discord.app_commands.tree: Ignoring exception in command 'link'
2026-04-09T17:16:16.770307109Z [err]    File "/opt/venv/lib/python3.11/site-packages/discord/abc.py", line 1618, in send
2026-04-09T17:16:16.770307135Z [err]  Traceback (most recent call last):
2026-04-09T17:16:16.770308642Z [err]  The above exception was the direct cause of the following exception:
2026-04-09T17:16:16.770315828Z [err]      data = await state.http.send_message(channel.id, params=params)
2026-04-09T17:16:16.770316177Z [err]    File "/opt/venv/lib/python3.11/site-packages/discord/app_commands/commands.py", line 858, in _do_call
2026-04-09T17:16:16.770323300Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-04-09T17:16:16.770324180Z [err]      return await self._callback(interaction, **params)  # type: ignore
2026-04-09T17:16:16.770332743Z [err]    File "/opt/venv/lib/python3.11/site-packages/discord/http.py", line 752, in request
2026-04-09T17:16:16.770333278Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-04-09T17:16:16.770338750Z [err]      raise Forbidden(response, data)
2026-04-09T17:16:16.770352841Z [err]  discord.errors.Forbidden: 403 Forbidden (error code: 50001): Missing Access
2026-04-09T17:16:16.770359075Z [err]  
2026-04-09T17:16:16.771918546Z [err]      return await self._do_call(interaction, transformed_values)
2026-04-09T17:16:16.771922471Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-04-09T17:16:16.771925550Z [err]    File "/opt/venv/lib/python3.11/site-packages/discord/app_commands/commands.py", line 876, in _do_call
2026-04-09T17:16:16.771928614Z [err]      raise CommandInvokeError(self, e) from e
2026-04-09T17:16:16.771931415Z [err]  discord.app_commands.errors.CommandInvokeError: Command 'link' raised an exception: Forbidden: 403 Forbidden (error code: 50001): Missing Access
