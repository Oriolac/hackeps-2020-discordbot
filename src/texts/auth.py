ALREADY_ON_GROUP_ERROR = "¡Ups! Por lo que veo ya estás en un equipo. Debes hacer `eps!leave` antes de poder unirte a uno nuevo"
NOT_REGISTERED_ERROR = "¡Ups! Parece que no estás conectado a tu cuenta de HackEPS. Escribe `eps!login` para volver a iniciar el proceso de registro."
def NOT_INGROUP_ERROR(author):
    return f"Parece que no apuntaste ningún grupo. Puedes usar los canales de reclutamiento para buscar equipo. Con el comando `eps!create` puedes crear un equipo o pídele a tus compañeros que te inviten mediante `eps!invite {author}`"