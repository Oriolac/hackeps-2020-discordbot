import logging

from discord.ext.commands import Context


class EitherCatching:

    def __init__(self, command: str, ctx: Context, text_module):
        self.command = command.upper()
        self.ctx = ctx
        self.texts = text_module

    def user_not_registered(self, user):
        if not user:
            logging.info(f"[COMMAND {self.command} - ERROR] Usuario no registrado")
            await self.ctx.send(self.texts.NOT_REGISTERED_ERROR)
            raise ValueError

    def already_in_group(self, user):
        if user.group_name is not None or user.group_name != '':
            logging.info(f"[COMMAND {self.command} - ERROR] El usuario ya se encuentra en un grupo")
            await self.ctx.send(self.texts.ALREADY_ON_GROUP_ERROR)
            raise ValueError

    def syntax_error(self, predicate, elem):
        if predicate(elem):
            logging.info(f"[COMMAND {self.command} - ERROR] La sintaxis es incorrecta")
            await self.ctx.send(self.texts.SINTAXIX_ERROR)
            raise ValueError

    def already_registered_team(self, group):
        if group:
            logging.info("[COMMAND CREATE - ERROR] El grupo indicado ya existe")
            await self.ctx.send(self.texts.GROUP_ALREADY_EXISTS_ERROR)
            raise ValueError


class InviteEitherCatching(EitherCatching):

    def not_in_team(self, team) -> bool:
        if not team:
            logging.error(f"{self.ctx.author.name} no tiene grupo")
            await self.ctx.send(self.texts.NOT_IN_GROUP)
            return